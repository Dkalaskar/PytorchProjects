import React, {useState, useRef} from 'react'
import "../style/image.css"


const ImageBox = () => {
    const [selectedImage, setSelectedImage] = useState(null);
  
    const handleImageUpload = (event) => {
      const file = event.target.files[0];
      const reader = new FileReader();
  
      reader.onload = (e) => {
        setSelectedImage(e.target.result);
      };
  
      reader.readAsDataURL(file);
    };
  
    const handlePredictClick = () => {
      // Implement your predict logic here
      console.log('Predict button clicked');
    };
  
    return (
      <div className="image-box">
        <div className="image-container">
          {selectedImage ? (
            <img src={selectedImage} alt="Uploaded" />
          ) : (
            <div className="placeholder">No image selected</div>
          )}
        </div>
        <div className="buttons">
          <input
            type="file"
            accept="image/*"
            id="upload-button"
            onChange={handleImageUpload}
          />
          <label htmlFor="upload-button">Upload</label>
          <button onClick={handlePredictClick}>Predict</button>
        </div>
      </div>
    );
  };
  
  export default ImageBox;