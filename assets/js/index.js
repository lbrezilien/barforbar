var ReactDOM = require('react-dom')
var Browseflow = require('./browseflow')
var App = require('./app')
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var SongList = require('./songlist')
var React = require('react')

ReactDOM.render(
                React.createElement(Router, null,
                  React.createElement(Route, {component: App},
                     React.createElement(Route, {path: "/", component: Browseflow}),
                     React.createElement(Route, {path: "mood/:name", component: SongList})

                  )
                ),
                 document.getElementById('react-app')
              )
