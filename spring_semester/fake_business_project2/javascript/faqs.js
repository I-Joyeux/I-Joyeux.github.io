const toggle = evt => {
    const linkElement = evt.currentTarget;                 // get the clicked link element
    const h3Element = linkElement.parentNode;              // get the h2 tag for the <a> tag
    const divElement = h3Element.nextElementSibling;     // get h2's sibling div

    if (h3Element.hasAttribute("class"))
    {
        h3Element.removeAttribute("class");
    }
    else 
    {
        h3Element.className="minus";
    }
    if (divElement.hasAttribute("class")) 
    {
        divElement.removeAttribute("class");
    } 
    else 
    {
        divElement.className="open";
    }
    evt.preventDefault();   // cancel default action of h2 tag's <a> tag
};

document.addEventListener("DOMContentLoaded", () => 
{
    // get the h3 tags
    const linkElements = faqs.querySelectorAll("#faqs a");
    
    // attach event handler for each h3 tag	    
    for (let linkElement of linkElements) 
    {
        linkElement.addEventListener("click", toggle);
    }
    // set focus on first h3 tag's <a> tag
    linkElements[0].focus();       
});