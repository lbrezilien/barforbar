module.exports = React.createClass({displayName: "exports",
   render: function(){
       return (
         React.createElement("div", null, 
         React.createElement("h1", null, "Hello, world."), 
         React.createElement("p", null, "these are my cards: ")

         )
       )
   }
})