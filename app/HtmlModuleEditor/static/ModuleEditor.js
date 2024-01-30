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

function updateIcon(fieldValue, idToUpdate,iframeid){

    var iframe = document.getElementById(iframeid)
    var elementInIframe = iframe.contentWindow.document.getElementById(idToUpdate);
    elementInIframe.classList.replace(elementInIframe.classList[1], fieldValue)
}

function updateLivePreview(fieldValue, item_id_to_update,attribute_to_update,iframe_id){
    var iframe = document.getElementById(iframe_id)
    var elementInIframe = iframe.contentWindow.document.getElementById(item_id_to_update);

        // This gets the ID of the incoming template
        // Gets the list of items that contain the specific class

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
                elementInIframe[attribute_to_update] = fieldValue
            }
            else
            {
                console.log("Invalid image URL");
            }
        }
        else
        {
            elementInIframe[attribute_to_update] = fieldValue
        }



}

function removeAllIdAttributes(htmlString) {
    // Create a temporary DOM element to parse the HTML string
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = htmlString;

    // Find all elements with an 'id' attribute
    const elementsWithId = tempDiv.querySelectorAll('[id]');

    // Remove the 'id' attribute from each element
    elementsWithId.forEach(element => element.removeAttribute('id'));

    // Return the modified HTML as a string
    return tempDiv.innerHTML;
}


    function displayHTMLCode(btnId, iframeBodyId, iframeId,removeIds){
    var iframe = document.getElementById(iframeId)
    var elementInIframeHTML = iframe.contentWindow.document.getElementById(iframeBodyId).innerHTML;
    if (removeIds){
        elementInIframeHTML = removeAllIdAttributes(elementInIframeHTML)
    }
    document.getElementById("staticBackdropLabel").innerText = 'HTML Code';
    document.getElementById("modal-body").innerText+= elementInIframeHTML;
    var HTMLModalElement = document.getElementById("staticBackdrop");
    var HTMLModal = new bootstrap.Modal(HTMLModalElement);
    HTMLModal.show();

    }


       function closeNav() {

    var sideNav = document.getElementById("sidenav");
    sideNav.style.display="none";

    var openBtn = document.getElementById("SideNavOpen");
    document.getElementById("content-body").style.marginLeft= "50px";
    openBtn.style.display="block";




    }
    function openNav(){
           var sideNav = document.getElementById("sidenav");
    sideNav.style.display="block";
    document.getElementById("content-body").style.marginLeft= "300px";
    document.getElementById("SideNavOpen").style.display="none"
    }