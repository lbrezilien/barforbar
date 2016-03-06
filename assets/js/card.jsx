var React = require('react')
var uselessVar = "";
var Link = require('react-router').Link

module.exports = React.createClass({
   moodGenreDict: {
        Happy:'smile-o',
        angry:'frown-o'
   },
   render: function(){
       return (

         <div className="col m3" >
             <div className="card">
               <div className="card-image discover" >
                 <img src={"/static/img/"+"happy.jpeg"}></img>
                 <div className="icon">
                    <i className={"fa fa-5x fa-"+this.moodGenreDict[""+this.props.mood.title+""]}></i>
                 </div>
               </div>
               <div className="card-action center-text">
               <Link to={"mood/"+this.props.mood.title}>
                   <span className="bold" >{this.props.mood.title}</span>
               </Link>
               </div>
             </div>

          </div>
       )
   }
})
