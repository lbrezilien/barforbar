var Card = require('./card')
var React = require('react')

module.exports = React.createClass({displayName: "exports",
  getInitialState: function(){
    return {moods: [], genres: []};
  },
  componentDidMount: function(){
       var component = this;
       $.get("http://localhost:8000/lyrics/moods", function(data){
         component.setState({moods: data});
       });

       $.get("http://localhost:8000/lyrics/genres", function(data){
          component.setState({genres: data});
        });
   },
   render: function(){
       return (React.createElement("div", {className: "row"},
                  React.createElement("div", {className: "row"},
                    React.createElement("h2", null, " Browse by Mood: "),
                    React.createElement("hr", null)
                  ),
                  React.createElement("div", {className: "row"},
                      this.state.moods.map(function(result) {
                          return React.createElement(Card, {key: result.pk, category: result, url: "moods"});
                      }),
                      React.createElement("hr", null)
                  ),
                  React.createElement("div", {className: "row"},
                    React.createElement("h2", null, " Browse by Genre: "),
                    React.createElement("hr", null)
                  ),
                  React.createElement("div", {className: "row"},
                    this.state.genres.map(function(result) {
                        return React.createElement(Card, {key: result.pk, category: result, url: "genres"});
                    }),
                    React.createElement("hr", null)
                  )
        ))
      }
    });
