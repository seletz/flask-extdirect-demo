Ext.define 'NXDirect.view.Demo',
    extend: 'Ext.grid.Panel'
    alias:  'widget.demo'

    columns: [
        dataIndex: 'id'
        text:      'ID'
        width:     50
    ,
        dataIndex: 'name'
        text:      'Name'
        flex:      1
        editor:
            allowBlank: no
            xtype: "textfield"
    ,
        dataIndex: 'number'
        text:      'Number'
        flex:      1
        editor:
            allowBlank: no
            xtype: "numberfield"
    ]

    store: "Direct"

    initComponent: ->
        console.log "DemoView::initComponent: view initialized"
        window.view = @

        rowEditing = Ext.create 'Ext.grid.plugin.RowEditing',
            clicksToMoveEditor: 1
            autoCancel: false

        @tbar = [
            text: "add"
            iconCls: "icon-add"
            itemId: "add"
            handler: =>
                console.log "add"
                rowEditing.cancelEdit()
                r = Ext.create "NXDirect.model.Demo",
                    name: "New"
                    number: 42

                NXDB.db_create r.getData(), (data) =>
                    r.setId(data.id)

                    @store.insert 0, r
                    rowEditing.startEdit r,0
        ,
            text: "remove"
            iconCls: "icon-delete"
            itemId: "remove"
            handler: =>
                console.log "remove"
                sm = @getSelectionModel()
                rowEditing.cancelEdit()
                @store.remove sm.getSelection()
                if store.getCount() > 0
                    sm.select 0
        ]
        @plugins = [rowEditing]

        @getSelectionModel().on "selectionchange", (selModel, selections) =>
            console.log "selectionchange", selModel, selections
            @down("#remove").setDisabled selections.length == 0


        @callParent(arguments)


# vim: set ft=coffee ts=4 sw=4 expandtab :

