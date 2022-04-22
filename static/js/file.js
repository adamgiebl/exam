const closeFileModal = () => {
  document.querySelector(".file-modal").style.display = "none";
};

const openFileModal = () => {
  document.querySelector(".file-modal").style.display = "grid";
  // Append Images Types Array Inisde Tooltip Data
  document.querySelector(".upload-area__tooltip-data").innerHTML = [
    ...imagesTypes,
  ].join(", .");
};

const imagesTypes = ["jpeg", "png", "svg", "gif"];

const onDrop = (el) => {
  console.log("drop");

  const file = el.dataTransfer.files[0];

  uploadFile(file);
};

const onClick = () => {
  console.log("onclick");
  document.querySelector("#fileInput").click();
};

const onChange = (el) => {
  const file = el.files[0];
  uploadFile(file);
};

// Upload File Function
function uploadFile(file) {
  // FileReader()
  const fileReader = new FileReader();
  // File Type
  const fileType = file.type;
  // File Size
  const fileSize = file.size;

  // If File Is Passed from the (File Validation) Function
  if (fileValidate(fileType, fileSize)) {
    // Add Class (drop-zone--Uploaded) on (drop-zone)
    document.querySelector("#dropZone").classList.add("drop-zone--Uploaded");

    // Show Loading-text
    document.querySelector("#loadingText").style.display = "block";
    // Hide Preview Image
    document.querySelector("#previewImage").style.display = "none";

    // Remove Class (uploaded-file--open) From (uploadedFile)
    document
      .querySelector("#uploadedFile")
      .classList.remove("uploaded-file--open");
    // Remove Class (uploaded-file__info--active) from (uploadedFileInfo)
    document
      .querySelector("#uploadedFileInfo")
      .classList.remove("uploaded-file__info--active");

    // After File Reader Loaded
    fileReader.addEventListener("load", function () {
      // After Half Second
      setTimeout(function () {
        // Add Class (upload-area--open) On (uploadArea)
        document
          .querySelector("#uploadArea")
          .classList.add("upload-area--open");

        // Hide Loading-text (please-wait) Element
        document.querySelector("#loadingText").style.display = "none";
        // Show Preview Image
        document.querySelector("#previewImage").style.display = "block";

        // Add Class (file-details--open) On (fileDetails)
        document
          .querySelector("#fileDetails")
          .classList.add("file-details--open");
        // Add Class (uploaded-file--open) On (uploadedFile)
        document
          .querySelector("#uploadedFile")
          .classList.add("uploaded-file--open");
        // Add Class (uploaded-file__info--active) On (uploadedFileInfo)
        document
          .querySelector("#uploadedFileInfo")
          .classList.add("uploaded-file__info--active");
      }, 500); // 0.5s

      // Add The (fileReader) Result Inside (previewImage) Source
      document
        .querySelector("#previewImage")
        .setAttribute("src", fileReader.result);

      // Add File Name Inside Uploaded File Name
      document.querySelector(".uploaded-file__name").innerHTML = file.name;

      // Call Function progressMove();
      progressMove();
    });

    // Read (file) As Data Url
    fileReader.readAsDataURL(file);
  } else {
    // Else

    this; // (this) Represent The fileValidate(fileType, fileSize) Function
  }
}

// Progress Counter Increase Function
function progressMove() {
  // Counter Start
  let counter = 0;

  // After 600ms
  setTimeout(() => {
    // Every 100ms
    let counterIncrease = setInterval(() => {
      // If (counter) is equle 100
      if (counter === 100) {
        // Stop (Counter Increase)
        clearInterval(counterIncrease);
      } else {
        // Else
        // plus 10 on counter
        counter = counter + 10;
        // add (counter) vlaue inisde (uploadedFileCounter)
        document.querySelector(
          ".uploaded-file__counter"
        ).innerHTML = `${counter}%`;
      }
    }, 100);
  }, 600);
}

// Simple File Validate Function
function fileValidate(fileType, fileSize) {
  // File Type Validation
  let isImage = imagesTypes.filter(
    (type) => fileType.indexOf(`image/${type}`) !== -1
  );

  // If The Uploaded File Is An Image
  if (isImage.length !== 0) {
    // Check, If File Size Is 2MB or Less
    if (fileSize <= 1000000) {
      // 2MB :)
      return true;
    } else {
      // Else File Size
      return alert("Please Your File Should be 1MB or Less");
    }
  } else {
    // Else File Type
    return alert("Please make sure to upload An Image File Type");
  }
}
