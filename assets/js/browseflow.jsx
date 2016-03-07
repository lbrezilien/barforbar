

var React = require('react')
var Card = require('./card')

module.exports = React.createClass({
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
       return (<div className="row">
                  <div className="row">
                    <h2> Browse by Mood: </h2>
                    <hr></hr>
                  </div>
                  <div className="row">
                      {this.state.moods.map(function(result) {
                          return <Card key={result.pk} category={result} url={"moods"} />;
                      })}
                      <hr></hr>
                  </div>
                  <div className="row">
                    <h2> Browse by Genre: </h2>
                    <hr></hr>
                  </div>
                  <div className="row" >
                    {this.state.genres.map(function(result) {
                        return <Card key={result.pk} category={result} url={"genres"}/>;
                    })}
                    <hr></hr>
                  </div>
        </div>)
      }
    });
