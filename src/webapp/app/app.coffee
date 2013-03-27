Ext.require([
    'Ext.direct.*',
    'Ext.data.*',
    'Ext.grid.*'
])

Ext.application
  controllers: ["Main"]
  views: ["Main"]
  name: "NXDirect"
  autoCreateViewport: true
  #require: ["Ext.direct.*"]
  launch: ->
      console.log "NXDirect.launch()"


Ext.onReady =>
  console.log "Ext.onReady"
  Ext.direct.Manager.addProvider Ext.app.REMOTING_API
