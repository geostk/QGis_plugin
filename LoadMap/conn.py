class Con:
  def loadLayer(self):
       self.mlr = None
       QgsMapLayerRegistry.instance().removeAllMapLayers()
       self.mlr = QgsMapLayerRegistry.instance()
       uri = QgsDataSourceURI()
       uri.setConnection("172.20.0.71", "5432", "ncrprs_db", "postgres", "123456")
       uri.setDataSource("recs", "t_parcel", "geometry", "")
       vlayer = QgsVectorLayer(uri.uri(), "Parcel", "postgres")
       if vlayer.isValid():
           self.mlr.addMapLayer(vlayer)
       else:
           QMessageBox.information(None, "Unable to Laod Data", "Unable to Load Layars from the Database!")
           return None
