Ext.define "NXDirect.controller.Main",
  extend: "Ext.app.Controller"

  stores: ["Direct"]
  models: ["Demo"]
  views:  ["Demo"]

  init: ->
      console.log "MainController::init", arguments
      window.controller = @
      window.store = @getDirectStore()

# vim: set ft=coffee ts=4 sw=4 expandtab :
