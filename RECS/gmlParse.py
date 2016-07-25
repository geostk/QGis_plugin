__author__ = 'Rob_G'
#from RECS.task_manager_dialog import TaskManagerDialog
class GMLParser:

	def createXML(self,taskID):
		import xml.dom.minidom
		#tskMgr=TaskManagerDialog()
		#print tskMgr.currentTaskLabel.text()
		doc = xml.dom.minidom.parse("Z:\\GMLFile\\%s.gml"%(taskID));
		parcels = doc.getElementsByTagName("Parcel")
		parcelsLength = parcels.length
		lstOID = []
		lstGEOMETRY = []
		lstBeginLifeSpan = []
		lstEndLifeSpan = []
		lstVoided = []
		lstSurveyed = []
		lstBlock_no = []
		lstStreet_no = []
		lstId = []
		lstSpatialUnitId = []
		lstParcelId = []
		lstUniqueParcelId = []
		lstTypeId = []
		lstArea = []
		lstArea_m = []
		lstArea_d = []
		lstPerimeter = []
		lstPerimeter_m = []
		lstPerimeter_d = []
		global j
		j=0

		for parcel in parcels:
			OID = parcel.getElementsByTagName('OID')[0]
			OIDValue = OID.childNodes[0].data
			lstOID.append(OIDValue)
			BeginLifespan = parcel.getElementsByTagName('BeginLifespan')[0]
			BeginLifespanValue = BeginLifespan.childNodes[0].data
			lstBeginLifeSpan.append(BeginLifespanValue)
			EndLifespan = parcel.getElementsByTagName('EndLifespan')[0]
			EndLifespanValue = EndLifespan.childNodes[0].data
			lstEndLifeSpan.append(EndLifespanValue)
			Voided = parcel.getElementsByTagName('Voided')[0]
			VoidedValue = Voided.childNodes[0].data
			lstVoided.append(VoidedValue)
			Surveyed = parcel.getElementsByTagName('Surveyed')[0]
			SurveyedValue = Surveyed.childNodes[0].data
			lstSurveyed.append(SurveyedValue)
			Id = parcel.getElementsByTagName('Id')[0]
			IdValue = Id.childNodes[0].data
			lstId.append(IdValue)
			SpatialUnitId = parcel.getElementsByTagName('SpatialUnitId')[0]
			SpatialUnitIdValue = SpatialUnitId.childNodes[0].data
			lstSpatialUnitId.append(SpatialUnitIdValue)
			ParcelId = parcel.getElementsByTagName('ParcelId')[0]
			ParcelIdValue = ParcelId.childNodes[0].data
			lstParcelId.append(ParcelIdValue)
			UniqueParcelId = parcel.getElementsByTagName('UniqueParcelId')[0]
			UniqueParcelIdValue = UniqueParcelId.childNodes[0].data
			lstUniqueParcelId.append(UniqueParcelIdValue)
			TypeId = parcel.getElementsByTagName('TypeId')[0]
			TypeIdValue = TypeId.childNodes[0].data
			lstTypeId.append(TypeIdValue)
			Area = parcel.getElementsByTagName('Area')[0]
			AreaValue = Area.childNodes[0].data
			lstArea.append(AreaValue)
			Perimeter = parcel.getElementsByTagName('Perimeter')[0]
			PerimeterValue = Perimeter.childNodes[0].data
			lstPerimeter.append(PerimeterValue)

			geoms = doc.getElementsByTagName("OGC_GEOMETRY")


			count = 0
			index = 0


			for geom in geoms:
				gmlPosList = geom.getElementsByTagName('gml:posList')[0]
				geomValue = gmlPosList.childNodes[0].data
				lstGEOMETRY.append(geomValue)


			while index < len(lstGEOMETRY[j]):
				index = lstGEOMETRY[j].find(' ', index)
				if index == -1:
					break
				else:
					count = count + 1
					if count % 2 != 0:
						lstGEOMETRY[j] = lstGEOMETRY[j][:index] + ',' + lstGEOMETRY[j][index + 1:]
				index += 1
			j+=1



		import xml.etree.ElementTree as xml
		filename = 'Z:\GMLFile\ogrGML.gml'
		root = xml.Element('FeatureCollection')
		root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
		root.set('xsi:schemaLocation', '')
		root.set('xmlns', 'http://ogr.maptools.org/')
		root.set('xmlns:gml', 'http://www.opengis.net/gml')
		for i in range(parcelsLength):
			featureMember = xml.SubElement(root, 'featureMember')
			ogrGML = xml.SubElement(featureMember, 'ogrGML')
			ogrGML.set('fid', 'ogrGML.0')
			geometryProperty = xml.SubElement(ogrGML, 'geometryProperty')
			Polygon = xml.SubElement(geometryProperty, 'Polygon')
			Polygon.set('srsName', 'EPSG:20137')
			outerBoundaryIs = xml.SubElement(Polygon, 'outerBoundaryIs')
			LinearRing = xml.SubElement(outerBoundaryIs, 'LinearRing')
			coordinates = xml.SubElement(LinearRing, 'coordinates')
			coordinates.text = lstGEOMETRY[i]
			OID = xml.SubElement(ogrGML, 'OID')
			OID.text = lstOID[i]
			BeginLifespan = xml.SubElement(ogrGML, 'BeginLifespan')
			BeginLifespan.text = lstBeginLifeSpan[i]
			EndLifespan = xml.SubElement(ogrGML, 'EndLifespan')
			EndLifespan.text = lstEndLifeSpan[i]
			Voided = xml.SubElement(ogrGML, 'Voided')
			Voided.text = lstVoided[i]
			Surveyed = xml.SubElement(ogrGML, 'Surveyed')
			Surveyed.text = lstSurveyed[i]
			Block_no = xml.SubElement(ogrGML, 'Block_no').set('xsi:nil', 'true')
			Street_no = xml.SubElement(ogrGML, 'Street_no xsi:nil="true"')
			Id = xml.SubElement(ogrGML, 'Id')
			Id.text = lstId[i]
			SpatialUnitId = xml.SubElement(ogrGML, 'SpatialUnitId')
			SpatialUnitId.text = lstSpatialUnitId[i]
			ParcelId = xml.SubElement(ogrGML, 'ParcelId')
			ParcelId.text = lstParcelId[i]
			UniqueParcelId = xml.SubElement(ogrGML, 'UniqueParcelId')
			UniqueParcelId.text = lstUniqueParcelId[i]
			TypeId = xml.SubElement(ogrGML, 'TypeId')
			TypeId.text = lstTypeId[i]
			Area = xml.SubElement(ogrGML, 'Area')
			Area.text = lstArea[i]
			Area_m = xml.SubElement(ogrGML, 'Area_m').set('xsi:nile', 'true')

			Area_d = xml.SubElement(ogrGML, 'Area_d').set('xsi:nil', 'true')
			Perimeter = xml.SubElement(ogrGML, 'Perimeter')
			Perimeter.text = lstPerimeter[i]
			Perimeter_m = xml.SubElement(ogrGML, 'Perimeter_m').set('xsi:nil', 'true')
			Perimeter_d = xml.SubElement(ogrGML, 'Perimeter_d').set('xsi:nil', 'true')
			HouseNumber = xml.SubElement(ogrGML, 'HouseNumber')
		tree = xml.ElementTree(root)
		with open(filename, "w") as fh:
			tree.write(fh,xml_declaration=True,encoding='utf-8',
					   method="xml")

	if __name__ == "__main__":
		createXML()
			#
			# import time
			# import xml.etree.cElementTree as ET
			# def editXML():
			# """
			#     Edit an example XML file
			#     """
			#     filename="F:\Shared\sample1.gml"
			#     tree = ET.ElementTree(file=filename)
			#     root = tree.getroot()
			#
			#     for begin_time in root.iter("posList"):
			#         begin_time.text='this is update' # begin_time.text = time.ctime(int(begin_time.text))
			#
			#     tree = ET.ElementTree(root)
			#     with open("F:\Shared\sample1.gml", "w") as f:
			#         tree.write(f)
			# if __name__ == "__main__":
			#     editXML()