// quill-setup.js

// Initialize Quill editor
var quill = new Quill('#editor', {
    theme: 'snow',
    modules: {
      toolbar: [
        [{ 'header': [1, 2, false] }],
        ['bold', 'italic', 'underline'],
        [{ 'list': 'ordered'}, { 'list': 'bullet' }],
        ['link'],
        ['clean']  // remove formatting button
      ]
    }
  });
  
  // Handle form submission by transferring the Quill content to the hidden textarea
  document.querySelector('form').onsubmit = function() {
    var body = document.querySelector('textarea[name=body]');
    body.value = quill.root.innerHTML;
  };
  
  // Update word count
  quill.on('text-change', function() {
    var text = quill.getText();
    var wordCount = text.trim().split(/\s+/).length;
    document.getElementById('word-count').innerText = 'Word Count: ' + wordCount;
  });
  