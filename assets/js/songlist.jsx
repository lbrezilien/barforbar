var React = require('react')

module.exports = React.createClass({
  getInitialState: function(){
      return {};
  },
  componentDidMount: function(){
      var component = this;
      $.get("http://localhost:8000/lyrics/moods", function(data){
        var songs = data.map(function(obj){
          if(obj.fields.title == "Happy"){
              return obj
           }
         });
        component.setState(songs[0].fields);
      });
  },
   render: function(){

       return (<div className="row">
                  <h1>{this.state.lyrics}</h1>
              </div>)
   }
})
