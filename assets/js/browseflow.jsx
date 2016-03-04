

var React = require('react')
var Card = require('./card')
var uselessVar = "";

module.exports = React.createClass({
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
       return (<div className="row">
                  <div className="row">
                    <h2> Browse by Mood: </h2>
                    <hr></hr>
                  </div>
                  <div className="row">
                      {this.state.data.map(function(result) {
                          return <Card key={result.pk} mood={result.fields} />;
                      })}
                      <hr></hr>
                  </div>
                  <div className="row">
                    <h2> Browse by Genre: </h2>
                    <hr></hr>
                  </div>
                  <div className="row" >
                    {this.state.data.map(function(result) {
                        return <Card key={result.pk} mood={result.fields} />;
                    })}
                    <hr></hr>
                  </div>
        </div>)
      }
    });
