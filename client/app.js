function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    // Log the input values to debug
    console.log("Square Footage: " + sqft.value);
    console.log("BHK: " + bhk);
    console.log("Bathrooms: " + bathrooms);
    console.log("Location: " + location.value);

    // Validate the inputs before sending to the backend
    if (isNaN(sqft.value) || parseFloat(sqft.value) <= 0) {
        estPrice.innerHTML = "<h2>Invalid Square Footage</h2>";
        console.error("Invalid square footage");
        return;
    }
    if (bhk < 1) {
        estPrice.innerHTML = "<h2>Invalid BHK value</h2>";
        console.error("Invalid BHK value");
        return;
    }
    if (bathrooms < 1) {
        estPrice.innerHTML = "<h2>Invalid Bathrooms value</h2>";
        console.error("Invalid bathrooms value");
        return;
    }
    if (!location.value) {
        estPrice.innerHTML = "<h2>Location is required</h2>";
        console.error("Location is required");
        return;
    }

    // Send the POST request
    var url = "https://bangalore-home-price-prediction-cp7r.onrender.com/predict_home_price";
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    }, function(data, status) {
        console.log(data);
        if (data.estimated_price !== undefined) {
            estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        } else {
            estPrice.innerHTML = "<h2>Price not available</h2>";
        }
    }).fail(function(xhr, status, error) {
        estPrice.innerHTML = "<h2>Error fetching price</h2>";
        console.error("Request failed: " + error);
    });
}




function onPageLoad() {
  console.log("document loaded");

  var url = "https://bangalore-home-price-prediction-cp7r.onrender.com/get_location_names";

  $.get(url, function(data, status) {
      console.log("got response for get_location_names request");
      if (data && data.locations) {
          var locations = data.locations;
          console.log("Available Locations:", locations); // Log available locations
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for (var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      } else {
          console.error("Location data not found");
      }
  }).fail(function(xhr, status, error) {
      console.error("Error fetching locations: " + error);
  });
}


window.onload = onPageLoad;
