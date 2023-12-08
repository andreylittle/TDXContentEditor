function updateFieldColor(field) {
    document.getElementById(field.id+"_txtvalue").innerHTML = field.value;
}

function updateDefaultedPreview(fieldValue, template_id, class_to_update, tag_to_update,id_to_update,attribute_to_update){

    if (class_to_update){
        // This gets the ID of the incoming template
        var templateToUpdate = document.getElementById(template_id)
        // Gets the list of items that contain the specific class
        var list_of_classes_to_update = templateToUpdate.getElementsByClassName(class_to_update)

        // Loops through all elements updating proper field
        for (let i=0; i<list_of_classes_to_update.length;i++){
            list_of_classes_to_update[i].style[attribute_to_update]=fieldValue;
        }
    }

    if (tag_to_update){
        // This gets the ID of the incoming template
        var templateToUpdate = document.getElementById(template_id)
        // Gets the list of items that contain the specific class
        var list_of_tags_to_update = templateToUpdate.getElementsByTagName(tag_to_update)

        // Loops through all elements updating proper field
        for (let i=0; i<list_of_tags_to_update.length;i++){
            list_of_tags_to_update[i].style[attribute_to_update]=fieldValue;
        }
    }
    // when editing ID,
    if (id_to_update){
        // This gets the ID of the incoming template
        // Gets the list of items that contain the specific class
        var item_id_to_update = document.getElementById(id_to_update)

        if (attribute_to_update==='src'){
            function validateImageURL(url) {
                if (url.trim()===""){
                    return true
                }
                // Regular expression to validate URL format
                var urlRegex = /^(ftp|http|https):\/\/[^ "]+$/;

                if (!urlRegex.test(url)) {
                    // Invalid URL format
                    return false;
                }
                else{

                return true;
                }
            }
            if (validateImageURL(fieldValue)) {
                item_id_to_update[attribute_to_update] = fieldValue
            }
            else
            {
                console.log("Invalid image URL");
            }
        }
        else
        {
            item_id_to_update[attribute_to_update] = fieldValue
        }

    }

}
