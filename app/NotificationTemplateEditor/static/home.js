function updateFieldColor(field) {
    var encodedValue = $("<div>").text(field.value).html();

    document.getElementById(field.id + "_txtvalue").innerHTML = encodedValue;
}


/**
 *
 * @param fieldValue this will always be set to (this.value)
 * @param template_id which ever template id there is to update, each template has a parent id and sub ids, we want to only send the parent id
 * @param class_to_update
 * @param tag_to_update -
 * @param id_to_update - this is expected to be an array, in some cases I might have multiple ids to update
 * @param attribute_to_update
 */
function updateDefaultedPreview(fieldValue, template_id, class_to_update, tag_to_update, id_to_update, attribute_to_update, sanitizeValue = true) {
    if (sanitizeValue) {
        fetch('http://127.0.0.1:5000/NotificationEditor/update_preview', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // Ensure this is set correctly
                },
                body: JSON.stringify({
                    "FieldValue": fieldValue
                })
            })

            .then(response => response.json()) // Parse JSON response
            .then(data => {
                console.log('Success:', data);
                var fieldValue = data.sanitizedValue;
                updateFieldAfterSanitization(fieldValue, template_id, class_to_update, tag_to_update, id_to_update, attribute_to_update)


            })
            .catch(error => {
                console.error('Error:', error);
            });
    } else {
        updateFieldAfterSanitization(fieldValue, template_id, class_to_update, tag_to_update, id_to_update, attribute_to_update)

    }




}




function updateFieldAfterSanitization(fieldValue, template_id, class_to_update, tag_to_update, id_to_update, attribute_to_update) {
    if (class_to_update) {

        var templateToUpdate = document.getElementById(template_id)
        // Gets the list of items that contain the specific class
        var list_of_classes_to_update = templateToUpdate.getElementsByClassName(class_to_update)

        // Loops through all elements updating proper field
        for (let i = 0; i < list_of_classes_to_update.length; i++) {
            list_of_classes_to_update[i].style[attribute_to_update] = fieldValue;
        }



        // This gets the ID of the incoming template

    }

    if (tag_to_update) {
        // This gets the ID of the incoming template
        var templateToUpdate = document.getElementById(template_id)
        // Gets the list of items that contain the specific class

        var list_of_tags_to_update = templateToUpdate.getElementsByTagName(tag_to_update)

        // Loops through all elements updating proper field
        for (let i = 0; i < list_of_tags_to_update.length; i++) {
            list_of_tags_to_update[i].style[attribute_to_update] = fieldValue;

        }
    }
    // when editing ID,
    if (id_to_update) {

        for (let i = 0; i < id_to_update.length; i++) {

            var item_id_to_update = document.getElementById(id_to_update[i])


            if (attribute_to_update === 'src') {
                function validateImageURL(url) {
                    if (url.trim() === "") {
                        return true
                    }
                    // Regular expression to validate URL format
                    var urlRegex = /^(ftp|http|https):\/\/[^ "]+$/;

                    if (!urlRegex.test(url)) {
                        // Invalid URL format
                        return false;
                    } else {

                        return true;
                    }
                }
                if (validateImageURL(fieldValue)) {
                    item_id_to_update[attribute_to_update] = fieldValue
                } else {
                    console.log("Invalid image URL");
                }
            } else {

                item_id_to_update[attribute_to_update] = fieldValue

            }
        }
        // This gets the ID of the incoming template
        // Gets the list of items that contain the specific class


    }
}

function collectFormData() {
    var forms = document.forms;
    var queryUrl = "http://127.0.0.1:5000/NotificationEditor/process?";

    for (var i = 0; i < forms.length; i++) {
        var form = forms[i];
        for (var j = 0; j < form.elements.length; j++) {
            var element = form.elements[j];
            if (element.name) {
                queryUrl += encodeURIComponent(element.name) + "=" + encodeURIComponent(element.value) + "&";
            }
        }
    }

    // Remove the last "&" from the queryUrl
    queryUrl = queryUrl.slice(0, -1);

    // Redirect to the constructed URL



}

function getPageData(){
    var formData = {};
    var forms = document.forms;

        for (var i = 0; i < forms.length; i++) {
        var form = forms[i];
        for (var j = 0; j < form.elements.length; j++) {
            var element = form.elements[j];
            if (element.name) {
                formData[element.name] = element.value;
            }
        }
    }
    var jsonString = JSON.stringify(formData);
    var encodedString = encodeURIComponent(jsonString);

        fetch('http://127.0.0.1:5000/NotificationEditor/save_values', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // Ensure this is set correctly
                },
                body: JSON.stringify({"data":encodedString})
            })

            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                var newTemplateId =data.template_id;
                var queryUrl = "http://127.0.0.1:5000/NotificationEditor/process?template_id=" +data.template_id
                //Set Modal Data
                document.getElementById("staticBackdropLabel").innerText= `Click to View Link`
document.getElementById("modal-body").innerHTML = `
  <a style="font-size: 20px; font-weight: bold; color: #8332a7;" href="${queryUrl}" target="_blank">Click to open shareable Link</a>
  <a style="color: #8332a7; font-size: 20px" role="button"  title="Copy URL" class="fa fa-clipboard" onclick="navigator.clipboard.writeText('${queryUrl}')"></a>
`;
            })
            .catch(error => {
                console.error('Error:', error);
            });

}


function closeAlert() {
    document.getElementById('customAlert').style.display = 'none';
}
window.onload = function() {
    // Function to get the value of a query parameter by name
    function getQueryParam(name) {
        name = name.replace(/[\[\]]/g, '\\$&');
        var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
            results = regex.exec(window.location.href);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, ' '));
    }
    // Function to check if the string is non-empty and not null
    function isNonEmptyString(str) {
        return str !== null && str.trim() !== '';
    }

    // Function to set form values based on URL parameters
    function setFormValues() {
        var forms = document.forms;
        for (var i = 0; i < forms.length; i++) {
            var form = forms[i];
            for (var j = 0; j < form.elements.length; j++) {
                var element = form.elements[j];
                if (element.name) {
                    var paramValue = getQueryParam(element.name);
                    if (isNonEmptyString(paramValue)) {
                        element.value = paramValue;
                        // Dispatch the oninput event
                        var event = new Event('input', {
                            bubbles: true,
                            cancelable: true,
                        });
                        element.dispatchEvent(event);
                    }
                }
            }
        }
    }

    // Set form values on page load
    setFormValues();
};