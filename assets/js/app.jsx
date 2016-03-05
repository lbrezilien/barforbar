var React = require('react')
var Browseflow = require('./browseflow')
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link


module.exports = React.createClass({
   render: function(){
       return (<div>
                  {this.props.children}
              </div>)
   }
})
