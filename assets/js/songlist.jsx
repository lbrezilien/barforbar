
var React = require('react')
module.exports = React.createClass({
  getInitialState: function(){
      return {songs: []};
  },
  componentDidMount: function(){
      var component = this;
      var api = "";
      if (this.props.route.path.indexOf('moods') >= 0)
        { api = 'moods' }
      else
        { api = 'genres'}
      $.get("http://localhost:8000/lyrics/"+api, function(data){
          var songs = data.filter(function(object){
              if(object.title == component.props.params.name){ return object}
            })
        component.setState({songs: songs[0].lyrics});
      });
  },
   render: function(){
       var comp = this;
       return (<div className="row card form-padding">
                <h2> {this.props.params.name} Songs: </h2>
                 <ul>

                </ul>

                <table className="highlight ">
                  <thead>
                    <tr>
                        <th data-field="SongTitle">Song Title</th>
                        <th data-field="Artist">Artist </th>
                        <th data-field="Lyrics">Lyrics </th>
                    </tr>
                  </thead>
                  <tbody>
                  {comp.state.songs.map(function(song){
                    return ( <tr key={song.pk}>
                                <td>{song.title}</td><td>{song.artist}</td>
                                <td>
                                <a href={"/lyrics/"+song.pk}><i className="material-icons">description</i></a>
                                </td>

                             </tr>)
                   })}
                  </tbody>
                </table>
              </div>)

   }
})
