const listImagesURL = 'http://127.0.0.1:5000/list_images';
const analyzeImage = 'http://127.0.0.1:5000/analyse_image/';

$(document).ready(function() {
    $("#getList").click(function(){
        $.ajax({url: listImagesURL, 
            success: function(result){
                let listImages = `<table class='m-3 p-3 table table-striped'>
                                    <thead>
                                        <tr>
                                            <th>Image name</th>
                                            <th>Analyse image</th>
                                        </tr>
                                    </thead>
                                    <tbody>`
                result.images.forEach(image => {
                    listImages += `<tr>
                                        <th scope="row">${image}</th>
                                        <td>
                                            <a class="links btn btn-primary" data-bs-toggle="collapse" data-bs-target="#collapse" href="http://127.0.0.1:5000/analyse_image/${image}">${image}</a>
                                        </td>
                                    </tr>`
                });
                listImages += "</tbody></table>"
                $("#list").html(listImages);

                $(".links").click(function(){
                    $.ajax({url: analyzeImage + this.text, 
                        success: function(result){
                            let res = `Width: ${result.width}, Height: ${result.height}`;
                            console.log(res);
                            $("#collapseProperties").text(res);
                      },
                    });
                });
          },
        });
   });


 });
