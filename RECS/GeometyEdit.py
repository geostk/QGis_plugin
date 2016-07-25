__author__ = 'Pc'
import xml.dom.minidom
class GeometryEdit():
    def split(self,doc_edited,doc_origion):
        # self.getEditedCoordinates(doc_edited)
        # print doc_origion
        # print doc_edited
        origin_geom = self.getOriginalOid(doc_origion)
        edited_geom = self.getEditedOid(doc_edited)
        print origin_geom
        print "\n"
        print edited_geom
        print "splited parcel OID is:"+self.getAffectedGeometries(edited_geom)
    def merge(self,doc_edited,doc_origion):
        origin_geom = self.getOriginalOid(doc_origion)
        edited_geom = self.getEditedOid(doc_edited)
        print origin_geom
        print "\n"
        print edited_geom
        #print set(doc_origion) - set(doc_edited)

        x = list(set(origin_geom) - set(edited_geom))
        print "merged parcels OID:"+x[0]+" and "+x[1]
        #print list(set(origin_geom).intersection(set(edited_geom)))
    def getOriginalOid(self,doc):
        lst_origion_Coordinates = []
        OriginOid = []
        doc_or = doc
        featMember = doc_or.getElementsByTagName("featureMember")
        for f in featMember:
            ogrGML = f.getElementsByTagName("ogrGML")
            oid = ogrGML[0].getElementsByTagName("OID")
            OriginOid.append(oid[0].childNodes[0].data)
            # geomProp = ogrGML[0].getElementsByTagName("geometryProperty")
            # polygon =  geomProp[0].getElementsByTagName("Polygon")
            # outBound = polygon[0].getElementsByTagName("outerBoundaryIs")
            # l_ring = outBound[0].getElementsByTagName("LinearRing")
            # coordinates = l_ring[0].getElementsByTagName("coordinates")
            # lst_origion_Coordinates.append( coordinates[0].childNodes[0].data)
            # print len(lst_origion_Coordinates)
        return OriginOid
    def getEditedOid(self,doc):
        lst_edited_Coordinates = []
        editedOid = []
        doc_or = doc
        featMember = doc_or.getElementsByTagName("gml:featureMember")
        for f in featMember:
            ogrGML = f.getElementsByTagName("ogr:temp")
            oid = ogrGML[0].getElementsByTagName("ogr:OID")
            editedOid.append(oid[0].childNodes[0].data)
            # geomProp = ogrGML[0].getElementsByTagName("ogr:geometryProperty")
            # polygon =  geomProp[0].getElementsByTagName("gml:Polygon")
            # outBound = polygon[0].getElementsByTagName("gml:outerBoundaryIs")
            # l_ring = outBound[0].getElementsByTagName("gml:LinearRing")
            # coordinates = l_ring[0].getElementsByTagName("gml:coordinates")
            # lst_edited_Coordinates.append( coordinates[0].childNodes[0].data)
            # print len(lst_edited_Coordinates)
        return editedOid
    def getAffectedGeometries(self,editedOid):
        oid_list=[]
        editedOid.sort()
        for i in range(0,len(editedOid)-1):
               if editedOid[i] == editedOid[i+1]:
                   oid_list.append(str(editedOid[i]))

        return oid_list[0]

