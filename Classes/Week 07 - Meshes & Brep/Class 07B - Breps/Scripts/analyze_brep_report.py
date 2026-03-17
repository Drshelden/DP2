"""
Rhino Python script: Analyze a selected Brep and print a detailed report.

What it reports:
- Brep object metadata (GUID, validity, counts)
- Face/surface details (type, area where possible, UV domains)
- Edge details (index, length, tolerance, valence, seam)
- Trim details and linked 2D parameter-space curve info
- Topology relationships:
  - For each edge, list the faces that share it
  - Print Rhino object GUID of the source Brep for each relationship

Notes:
- Faces inside one Brep are sub-entities and do not have independent Rhino object IDs.
  Their stable identity within the Brep is FaceIndex.
"""

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino


def guid_to_string(g):
    try:
        return str(g)
    except Exception:
        return "<invalid-guid>"


def surface_type_name(surface):
    if surface is None:
        return "Unknown"

    # Most RhinoCommon surfaces are subclasses of Surface and expose GetType().Name.
    try:
        return surface.GetType().Name
    except Exception:
        return "Surface"


def valence_name(valence):
    # Rhino.Geometry.EdgeAdjacency enum values are usually None, Naked, Interior, NonManifold
    try:
        return str(valence)
    except Exception:
        return "Unknown"


def safe_area(face):
    try:
        amp = Rhino.Geometry.AreaMassProperties.Compute(face)
        if amp:
            return amp.Area
    except Exception:
        pass
    return None


def edge_is_seam_from_trims(edge, brep_geom):
    # An edge is a seam if it has two (or more) trims on the same face.
    edge_index = edge.EdgeIndex
    face_hits = []
    for trim in brep_geom.Trims:
        if trim.Edge and trim.Edge.EdgeIndex == edge_index and trim.Face:
            face_hits.append(trim.Face.FaceIndex)

    return len(face_hits) != len(set(face_hits))


def report_brep(brep_obj_ref):
    rh_obj = brep_obj_ref.Object()
    brep_geom = brep_obj_ref.Brep()

    if rh_obj is None or brep_geom is None:
        print("Could not resolve selected object as a Brep.")
        return

    brep_id = rh_obj.Id

    print("=" * 80)
    print("BREP REPORT")
    print("=" * 80)
    print("Brep Rhino Object ID: {}".format(guid_to_string(brep_id)))
    print("IsValid: {}".format(brep_geom.IsValid))
    print("Solid: {}".format(brep_geom.IsSolid))
    print("Manifold: {}".format(brep_geom.IsManifold))
    print("Face count: {}".format(brep_geom.Faces.Count))
    print("Edge count: {}".format(brep_geom.Edges.Count))
    print("Trim count: {}".format(brep_geom.Trims.Count))
    print("Loop count: {}".format(brep_geom.Loops.Count))
    print("Vertex count: {}".format(brep_geom.Vertices.Count))
    print("Surface count: {}".format(brep_geom.Surfaces.Count))

    print("\n" + "-" * 80)
    print("FACES / SURFACES")
    print("-" * 80)
    for face in brep_geom.Faces:
        srf = face.UnderlyingSurface()
        srf_name = surface_type_name(srf)
        area = safe_area(face)

        udom = face.Domain(0)
        vdom = face.Domain(1)

        print("FaceIndex: {}".format(face.FaceIndex))
        print("  OrientationReversed: {}".format(face.OrientationIsReversed))
        print("  SurfaceType: {}".format(srf_name))
        print("  SurfaceIndex: {}".format(face.SurfaceIndex))
        print("  LoopCount: {}".format(face.Loops.Count))
        print("  U Domain: [{:.6g}, {:.6g}]".format(udom.T0, udom.T1))
        print("  V Domain: [{:.6g}, {:.6g}]".format(vdom.T0, vdom.T1))
        if area is not None:
            print("  Area: {:.6g}".format(area))
        else:
            print("  Area: <unavailable>")

    print("\n" + "-" * 80)
    print("EDGES")
    print("-" * 80)
    for edge in brep_geom.Edges:
        edge_index = edge.EdgeIndex

        # Adjacent faces by topology index
        face_indices = list(edge.AdjacentFaces())

        print("EdgeIndex: {}".format(edge_index))
        print("  Length: {:.6g}".format(edge.GetLength()))
        print("  Tolerance: {:.6g}".format(edge.Tolerance))
        print("  Valence: {}".format(valence_name(edge.Valence)))
        print("  IsSeam: {}".format(edge_is_seam_from_trims(edge, brep_geom)))
        print("  AdjacentFaceIndices: {}".format(face_indices))

        # Relationship documentation requested by user:
        # edge -> (Brep object id + joined faces)
        print("  Joined Surface References:")
        if face_indices:
            for fi in face_indices:
                print(
                    "    BrepObjectID={} FaceIndex={}".format(
                        guid_to_string(brep_id), fi
                    )
                )
        else:
            print("    <none>")

    print("\n" + "-" * 80)
    print("TRIMS / 2D CURVES")
    print("-" * 80)
    for trim in brep_geom.Trims:
        trim_idx = trim.TrimIndex
        edge_idx = trim.Edge.EdgeIndex if trim.Edge else None
        face_idx = trim.Face.FaceIndex if trim.Face else None

        trim_2d = trim.TrimCurve
        trim_2d_type = surface_type_name(trim_2d)

        print("TrimIndex: {}".format(trim_idx))
        print("  TrimType: {}".format(trim.TrimType))
        print("  IsoStatus: {}".format(trim.IsoStatus))
        print("  FaceIndex: {}".format(face_idx))
        print("  EdgeIndex: {}".format(edge_idx))
        print("  2DCurveType: {}".format(trim_2d_type))
        if trim_2d:
            try:
                print("  2DCurveDomain: [{:.6g}, {:.6g}]".format(trim_2d.Domain.T0, trim_2d.Domain.T1))
                print("  2DCurveLength: {:.6g}".format(trim_2d.GetLength()))
            except Exception:
                print("  2DCurveDomain: <unavailable>")
                print("  2DCurveLength: <unavailable>")

    print("\n" + "-" * 80)
    print("EDGE -> JOINED SURFACES SUMMARY")
    print("-" * 80)
    for edge in brep_geom.Edges:
        face_indices = list(edge.AdjacentFaces())
        if face_indices:
            joined = ", ".join(["FaceIndex {}".format(fi) for fi in face_indices])
        else:
            joined = "<none>"

        print(
            "Edge {} -> BrepObjectID {} -> {}".format(
                edge.EdgeIndex,
                guid_to_string(brep_id),
                joined,
            )
        )

    print("\nReport complete.")


def main():
    obj_ref = rs.GetObject(
        message="Select one Brep to analyze",
        filter=rs.filter.polysurface | rs.filter.surface,
        preselect=True,
        select=False,
        custom_filter=None,
        subobjects=False,
    )

    if not obj_ref:
        print("No Brep selected.")
        return

    # Convert selected object to RhinoCommon ObjRef for robust Brep access.
    rhino_obj_ref = Rhino.DocObjects.ObjRef(obj_ref)
    report_brep(rhino_obj_ref)

    sc.doc.Views.Redraw()


if __name__ == "__main__":
    main()
