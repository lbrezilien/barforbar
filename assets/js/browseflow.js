var Card = require('./card')
var uselessVar = "";
var React = require('react')

module.exports = React.createClass({displayName: "exports",
  getInitialState: function(){
    return {data: []};
  },
  componentDidMount: function(){
       var component = this;
       $.get("http://localhost:8000/lyrics/moods", function(data){
         component.setState({data: data});
       });
   },
   render: function(){
       return (React.createElement("div", {className: "row"},
                  React.createElement("div", {className: "row"},
                    React.createElement("h2", null, " Browse by Mood: "),
                    React.createElement("hr", null)
                  ),
                  React.createElement("div", {className: "row"},
                      this.state.data.map(function(result) {
                          return React.createElement(Card, {key: result.pk, mood: result});
                      }),
                      React.createElement("hr", null)
                  ),
                  React.createElement("div", {className: "row"},
                    React.createElement("h2", null, " Browse by Genre: "),
                    React.createElement("hr", null)
                  ),
                  React.createElement("div", {className: "row"},
                    this.state.data.map(function(result) {
                        return React.createElement(Card, {key: result.pk, mood: result});
                    }),
                    React.createElement("hr", null)
                  )
        ))
      }
    });
