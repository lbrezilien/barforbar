var React = require('react')

module.exports = React.createClass({
  getInitialState: function(){
      return {songs: []};
  },
  componentDidMount: function(){
      var component = this;
      $.get("http://localhost:8000/lyrics/moods", function(data){
          var songs = data.filter(function(object){
              if(object.title == component.props.params.name){ return object}
            })
        component.setState({songs: songs[0].lyrics});
      });
  },
   render: function(){
       var comp = this;
       return (<div className="row">
                 <ul>
                    {comp.state.songs.map(function(song){
                      return (<li key={song.pk}>Song Title: {song.title}, Artist: {song.artist}</li>)
                    })}
                </ul>
              </div>)

   }
})
