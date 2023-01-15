const uploadImage = "http://127.0.0.1:5000/upload_image";
const listImagesURL = "http://127.0.0.1:5000/list_images";
const analyzeImage = "http://127.0.0.1:5000/analyse_image/";

// JQuery
$(document).ready(() => {
  // Event listener for loading the image list
  $("#getList").click(() => {
    // AJAX Petition to load the list
    $("#list").stop();
    $.ajax({
      url: listImagesURL,
      success: (result) => {
        if(result.images.length == 0){
          $("#list").stop().addClass("alert alert-danger");
          $("#list").text("There's no files stored").fadeIn().delay(1500).fadeOut();
        } else {
          let listImages = `<table class="table table-striped" style="table-layout:fixed;">
                              <thead>
                                <tr>
                                    <th>Image name</th>
                                    <th>Analyse image</th>
                                    <th>Properties</th>
                                </tr>
                              </thead>
                              <tbody>`;
        result.images.forEach((image) => {
          listImages += `<tr>
                            <th scope="row">${image}</th>
                            <td>
                                <a class="links btn btn-primary"" href="http://127.0.0.1:5000/analyse_image/${image}">ShowProperties: ${image}</a>
                            </td>
                            <td>
                                <div id="collapse${image}">
                                </div>  
                            </td>
                        </tr>`;
        });
        listImages += "</tbody></table>";
        $("#list").removeClass().text("").fadeIn();
        $("#list").html(listImages);
      }
        // Event listener for the analyzing buttons.
        // Show or collapse the width and height of the image on the correspondent properties cell.
        $(".links").click(function (e) {
          e.preventDefault();
          let imgNumber = this.text.split(" ")[1];
          target = `#collapse${imgNumber}`;
          $(target).text("").fadeOut(1);
          $.ajax({
            url: analyzeImage + imgNumber,
            success: (result) => {
              let res = `Width: ${result.width}, Height: ${result.height}`;
              console.log(res);
              $(target).text(res);
              $(target).fadeIn().delay(1500).fadeOut();
            },
            error: () => {
              $("#list").addClass("alert alert-danger");
              $("#list").text("There's an error. No response.").fadeIn().delay(1500).fadeOut();
            },
          });
        });
      },
      error: () => {
        $("#list").addClass("alert alert-danger");
        $("#list").text("There's an error. No response.").fadeIn().delay(1500).fadeOut();
      },
    });
  });

  // Action to sending the file
  $("#flash").removeClass().text("").fadeOut(1);

  $("form").submit((e) => {
    e.preventDefault();
    $("#flash").stop().removeClass().text("").fadeOut(1).stop();

    var form_data = new FormData($('#inputFile')[0]);
    $.ajax({
      type: 'POST',
      url: uploadImage,
      data: form_data,
      contentType: false,
      processData: false,
      statusCode: {
        201: (result) => {
          $("#flash").addClass("alert alert-success");
          $("#flash").text(result.message);
          $("#flash").fadeIn().delay(1500).fadeOut();
        }, 
        400: () =>{
          $("#flash").addClass("alert alert-danger");
          $("#flash").text("There's no file selected");
        },
        415: () =>{ 
          $("#flash").addClass("alert alert-danger");
          $("#flash").text("Only .jpg, .jpeg and .png extensions allowed");
        }
      }, error: () => {
          $("#flash").addClass("alert alert-danger");
          $("#flash").text("There's an error. No response.");
          $("#flash").fadeIn().delay(1500).fadeOut();
        }
    });
  });
});
