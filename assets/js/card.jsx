var React = require('react')
var uselessVar = "";
var Link = require('react-router').Link

module.exports = React.createClass({
   render: function(){
       return (

         <div className="col m2 card blue-grey darken-1" style={{marginRight:'10%'}}>
            <div className="card-content white-text">
            <Link to={"mood/"+this.props.mood.title}>
              <span className="card-title flow-text">{this.props.mood.title}</span>
            </Link>
            </div>
          </div>
       )
   }
})
