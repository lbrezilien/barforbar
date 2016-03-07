var React = require('react')
var Link = require('react-router').Link

module.exports = React.createClass({
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
     "R&B":'gratipay',
     "Jazz":'music',
     "Wierd":'moon-o',
     "Blues":'cloud',
     "Pop":'magic',
     "Spoken Word":'microphone',
     "Other":'question'

   },
   render: function(){
       return (

         <div className="col m3" >
             <div className="card">
               <div className="card-image discover" >
                 <img src={"/static/img/"+"happy.jpeg"}></img>
                 <div className="icon">
                    <i className={"fa fa-5x fa-"+this.moodGenreDict[""+this.props.category.title+""]}></i>
                 </div>
               </div>
               <div className="card-action center-text">
               <Link to={this.props.url+"/"+this.props.category.title} apiRoute={this.props.url}>
                   <span className="bold" >{this.props.category.title}</span>
               </Link>
               </div>
             </div>

          </div>
       )
   }
})
