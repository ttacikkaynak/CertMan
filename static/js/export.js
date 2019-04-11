// Code goes here

$(document).ready(function(){
  var table = $('#example').DataTable();

  $('#btn-export').on('click', function(){
      $('<table>').append(table.$('tr').clone()).table2excel({
          exclude: ".excludeThisClass",
          name: "Worksheet Name",
          filename: "SomeFile" //do not include extension
      });
  });
})
