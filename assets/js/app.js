var Browseflow = require('./browseflow')
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var React = require('react')


module.exports = React.createClass({displayName: "exports",
   render: function(){
       return (React.createElement("div", null,
                  this.props.children
              ))
   }
})
