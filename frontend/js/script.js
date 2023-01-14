const listImagesURL = "http://127.0.0.1:5000/list_images";
const analyzeImage = "http://127.0.0.1:5000/analyse_image/";

// JQuery
$(document).ready(function () {
  // Event listener for loading the image list
  $("#getList").click(() => {
    // AJAX Petition to load the list
    $.ajax({
      url: listImagesURL,
      success: (result) => {
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
                                            <a class="links btn btn-primary" data-bs-toggle="collapse" data-bs-target="#collapse${image}" href="http://127.0.0.1:5000/analyse_image/${image}">Click ${image}</a>
                                        </td>
                                        <td>
                                            <div class="collapse" id="collapse${image}">
                                                <div class="text-nowrap" id="collapseProperties${image}"></div>
                                            </div>  
                                        </td>
                                    </tr>`;
        });
        listImages += "</tbody></table>";
        $("#list").html(listImages);

        // Event listener for the analyzing buttons.
        // Show or collapse the width and height of the image on the correspondent properties cell.
        $(".links").click(function () {
          let imgNumber = this.text.split(" ")[1];
          $.ajax({
            url: analyzeImage + imgNumber,
            success: (result) => {
              let res = `Width: ${result.width}, Height: ${result.height}`;
              console.log(res);
              $("#collapseProperties" + imgNumber).text(res);
            },
            error: () => {
              $("#collapseProperties" + imgNumber).text("Show error"); // ERROR
            },
          });
        });
      },
      error: () => {
        $("#list").html("There's an error"); // ERROR
      },
    });
  });
});
