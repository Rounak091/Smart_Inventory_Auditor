# Smart Inventory Auditor

A web application that uses AI to analyze inventory images and provide real-time stock information and recommendations.

## Features

- **AI-Powered Image Analysis**: Uses Google Gemini AI to identify items from uploaded images
- **Inventory Lookup**: Automatically checks current stock levels and status
- **Real-time Recommendations**: Provides actionable insights for inventory management
- **Web Interface**: Simple HTML frontend for easy image upload and result viewing

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. **Clone or download the project files**

2. **Set up the virtual environment:**
   ```bash
   cd backend
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - On Windows (Command Prompt):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```

## Configuration

1. **Set up your API key:**
   - Open the `.env` file in the root directory
   - Replace `your_api_key_here` with your actual Google Gemini API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## Running the Application

1. **Start the backend server:**
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

   The server will start on `http://127.0.0.1:8000`

2. **Open the frontend:**
   - Open `frontend/index.html` in your web browser
   - Or serve it through a local web server if needed

## Usage

1. Open the frontend in your browser
2. Click "Choose File" to select an inventory image
3. Click "Analyze" to process the image
4. View the results showing:
   - Detected item
   - Category
   - Current inventory status
   - Quantity
   - Recommended action

## Project Structure

```
smart-inventory-auditor/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes.py          # API endpoints
│   │   │   └── __init__.py
│   │   ├── core/
│   │   │   ├── config.py          # Configuration settings
│   │   │   ├── gemini.py          # AI model setup
│   │   │   └── __init__.py
│   │   ├── db/
│   │   │   ├── inventory.py       # Inventory database
│   │   │   └── __init__.py
│   │   ├── services/
│   │   │   ├── auditor_agent.py   # Main AI processing logic
│   │   │   ├── inventory_service.py # Inventory lookup service
│   │   │   └── __init__.py
│   │   ├── main.py                # FastAPI application
│   │   └── __init__.py
│   ├── uploads/                   # Uploaded images storage
│   ├── venv/                      # Virtual environment (created)
│   └── craete_test_image.py       # Test image generator
├── frontend/
│   └── index.html                 # Web interface
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables
└── README.md                      # This file
```

## API Endpoints

- `GET /` - Health check endpoint
- `POST /audit` - Upload and analyze inventory image

## Sample Inventory Data

The application includes sample inventory data for:
- Laptop
- Keyboard
- Mouse
- Monitor

## Testing

1. **Generate a test image:**
   ```bash
   cd backend
   python craete_test_image.py
   ```

2. **Use the generated test image** (`test_inventory_image.png`) to test the application

## Troubleshooting

### Common Issues:

1. **"uvicorn command not found"**
   - Make sure you're in the activated virtual environment
   - Run `pip install -r ../requirements.txt` again

2. **"API key not valid"**
   - Check that your GEMINI_API_KEY in `.env` is correct
   - Ensure you have access to Google Gemini API

3. **CORS errors in browser**
   - Make sure the backend is running on `http://127.0.0.1:8000`
   - The frontend is configured to connect to this address

4. **Image upload fails**
   - Check that the `uploads` directory exists
   - Ensure the image file is not corrupted

## Development

### Adding New Inventory Items

Edit `backend/app/db/inventory.py` to add new items:

```python
INVENTORY_DB = {
    "new_item": {
        "category": "Category Name",
        "quantity": 10,
        "status": "In Stock",
        "reorder_level": 5
    }
}
```

### Modifying AI Prompts

Update the `SYSTEM_PROMPT` in `backend/app/core/gemini.py` to change AI behavior.

## License

This project is for educational and demonstration purposes.

## Support

For issues or questions, please check the troubleshooting section or examine the code comments for more details.
