var React = require('react');

module.exports = React.createClass({displayName: "exports",
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
       return (React.createElement("div", {className: "row card form-padding"},
                React.createElement("h2", null, " ", this.props.params.name, " Songs: "),
                 React.createElement("ul", null

                ),

                React.createElement("table", {className: "highlight "},
                  React.createElement("thead", null,
                    React.createElement("tr", null,
                        React.createElement("th", {"data-field": "SongTitle"}, "Song Title"),
                        React.createElement("th", {"data-field": "Artist"}, "Artist "),
                        React.createElement("th", {"data-field": "Lyrics"}, "Lyrics ")
                    )
                  ),
                  React.createElement("tbody", null,
                  comp.state.songs.map(function(song){
                    return ( React.createElement("tr", {key: song.pk},
                                React.createElement("td", null, song.title), React.createElement("td", null, song.artist),
                                React.createElement("td", null,
                                React.createElement("a", {href: "/lyrics/"+song.pk}, React.createElement("i", {className: "material-icons"}, "description"))
                                )

                             ))
                   })
                  )
                )
              ))

   }
})
