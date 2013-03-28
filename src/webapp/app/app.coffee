Ext.require([
    'Ext.direct.*',
    'Ext.data.*',
    'Ext.grid.*'
])

Ext.application
  controllers: ["Main"]
  name: "NXDirect"
  autoCreateViewport: true
  launch: ->
      console.log "NXDirect.launch()"
      window.controller = @getController "Main"


Ext.onReady =>
  console.log "Ext.onReady"
  Ext.direct.Manager.addProvider Ext.app.REMOTING_API

window.doit = ->
    NXDirect.model.Demo.load 5,
        scope: @
        callback: (rec, op) -> console.log "callback", rec, op
        failure: (rec, op) -> console.log "failure", rec, op
        success: (rec, op) -> console.log "success", rec, op
