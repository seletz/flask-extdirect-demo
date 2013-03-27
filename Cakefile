{spawn, exec} = require 'child_process'
util = require 'util'

app_name = "know"
wc_dir   = "/Volumes/D\$/ptc/Windchill/codebase/netmarkets/jsp/nexiles/#{app_name}"
static_dir = "static"

runCommand = (name, args...) ->
    proc =           spawn name, args
    proc.stderr.on   'data', (buffer) -> console.log buffer.toString()
    proc.stdout.on   'data', (buffer) -> console.log buffer.toString()
    proc.on          'exit', (status) ->
        util.log "ERROR: #{name} => #{status}" if status isnt 0
        process.exit(1) if status isnt 0

task "make_app", 'create and upload a nexiles|elements app', (options) ->
  runCommand 'coffee', '--output', 'static/js/', '-c', 'src/'
  runCommand 'nxtools', 'app-pack', '--name', app_name
  runCommand 'nxtools', 'app-upload', '--name', app_name

task 'init', 'initialize static dir with vendor data', (options) ->
  util.log "Copying vendor data files ..."
  #runCommand 'cp', 'vendor/extjs-4.1.1/ext-all.js', 'static/js/'
  #runCommand 'rsync', '-av', 'vendor/extjs-4.1.1/resources', 'static'
  #runCommand 'rsync', '-av', 'vendor/extjs-4.1.1/examples/ux', 'static/js'

task 'wcsync', 'initialize static dir with vendor data', (options) ->
  util.log "syncing static dir to WC dir"
  runCommand 'mkdir', '-p', wc_dir
  runCommand 'rsync', '-av', static_dir, wc_dir

task 'build', 'Watch source files and build JS & CSS', (options) ->
  invoke 'init'
  util.log "running build to static dir ..."
  runCommand 'coffee', '--output', static_dir, '-wc', 'src/'

task 'wcbuild', 'Watch source files and build JS to Windchill', (options) ->
  invoke 'init'
  invoke 'wcsync'
  util.log "running build to WC dir ..."
  runCommand 'coffee', '--output', "#{wc_dir}/", '-wc', 'src/'


