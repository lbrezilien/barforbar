var uselessVar = "";
var Link = require('react-router').Link
var React = require('react')

module.exports = React.createClass({displayName: "exports",
   render: function(){
       return (

         React.createElement("div", {className: "col m2 card blue-grey darken-1", style: {marginRight:'10%'}},
            React.createElement("div", {className: "card-content white-text"},
            React.createElement(Link, {to: "mood/"+this.props.mood.title},
              React.createElement("span", {className: "card-title flow-text"}, this.props.mood.title)
            )
            )
          )
       )
   }
})
