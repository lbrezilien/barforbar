var uselessVar = "";
var Link = require('react-router').Link
var React = require('react')

module.exports = React.createClass({displayName: "exports",
   moodGenreDict: {
     "Happy":'smile-o',
     "Just Chill":'meh-o',
     "Ice Cream Sad":'thumbs-down',
     "Feel Good":'reddit-alien',
     "Butterflies":'bug',
     "Head Banging":'bolt',
     "Swagged Out":'fighter-jet',
     "Inspirational":'beer',
     "Confidence Boost":'exclamation',
     "Hip Hop":'headphones',
     "Rock":'bolt',
     "R&B":'gratiplay',
     "Jazz":'music',
     "Wierd":'moon-o',
     "Blues":'cloud',
     "Pop":'magic',
     "Spoken Word":'microphone',
     "Other":'question'
   },
   render: function(){
       return (

         React.createElement("div", {className: "col m3"},
             React.createElement("div", {className: "card"},
               React.createElement("div", {className: "card-image discover"},
                 React.createElement("img", {src: "/static/img/"+"happy.jpeg"}),
                 React.createElement("div", {className: "icon"},
                    React.createElement("i", {className: "fa fa-5x fa-"+this.moodGenreDict[""+this.props.mood.title+""]})
                 )
               ),
               React.createElement("div", {className: "card-action center-text"},
               React.createElement(Link, {to: "mood/"+this.props.mood.title},
                   React.createElement("span", {className: "bold"}, this.props.mood.title)
               )
               )
             )

          )
       )
   }
})
