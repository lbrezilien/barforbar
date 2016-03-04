var React = require('react')
var ReactDOM = require('react-dom')
var Browseflow = require('./browseflow')
var App = require('./app')
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var SongList = require('./songlist')

ReactDOM.render(
                <Router >
                  <Route component={App} >
                     <Route path="/" component={Browseflow} />
                     <Route path="mood/:name" component={SongList} />

                  </Route>
                </Router>,
                 document.getElementById('react-app')
              )
