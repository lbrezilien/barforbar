var React = require('react')

var Card = require('./card')

module.exports = React.createClass({displayName: "exports",
   render: function(){
       return (React.createElement("div", {className: "row"}, React.createElement(Card, null)))
   }
})
