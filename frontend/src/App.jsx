import { useState } from "react";

export default function CSVUpload() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false)
  const [res, setData] = useState(null)

  const handleFileChange = (e) => {
    setError("");

    const selectedFile = e.target.files[0];

    if (!selectedFile) {
      setFile(null);
      return;
    }

    if (!selectedFile.name.toLowerCase().endsWith(".csv")) {
      setError("Please select a CSV file.");
      setFile(null);
      e.target.value = "";
      return;
    }

    setFile(selectedFile);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setData(null)

    if (!file) {
      setError("Please select a CSV file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true)
      const response = await fetch("http://localhost:8000/test/test", {
        method: "POST",
        body: formData,
      });

      const res = await response.json();

      console.log(res);
      setData(res)
      alert("File uploaded successfully!");
      setLoading(false)
      // setData(null)
    } catch (err) {
      console.error(err);
      alert("Upload failed.");
      setLoading(false)
    }
  };

  return (
    <div className=" flex flex-col font-serif ">
      <div className="max-w-md mx-auto mt-10 rounded-lg border p-6 shadow">
      <h2 className="mb-4 text-2xl font-bold">Upload CSV</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".csv,text/csv"
          onChange={handleFileChange}
          className="mb-4 w-full"
        />

        {file && (
          <div className="mb-4 rounded bg-gray-100 p-3">
            <p>
              <strong>File:</strong> {file.name}
            </p>
            <p>
              <strong>Size:</strong>{" "}
              {(file.size / 1024).toFixed(2)} KB
            </p>
          </div>
        )}

        {error && (
          <p className="mb-4 text-sm text-red-600">
            {error}
          </p>
        )}

        <button
          type="submit"
          disabled={!file || loading}
          className="w-full rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-gray-400"
        >
          { loading ?
          (
            <div className="flex flex-col justify-center items-center">
              <span className="w-10 h-10 border-2 border-blue-400 border-t-0 animate-spin transition-all duration-500 rounded-full"></span>
            </div>

          ):(
            <span>Submit</span>
        ) }
        </button>
      </form>
      </div>

      <div className="max-w-2xl mx-auto mt-10 rounded-lg flex flex-col h-124 ">
  {res && (
    <>
      <h2 className="text-center text-2xl rounded-lg p-2 border border-gray-500">{res.message}</h2>
      <div className="h-108 w-lg overflow-auto scrollbar-none">
      {res.data?.map((item, idx) => (
        <div
          key={idx}
          className="border rounded p-3 my-2"
        >
          <p><strong>Row:</strong> {item.row}</p>
          <p><strong>From:</strong> {item.From}</p>
          <p><strong>To:</strong> {item.To}</p>
          <p><strong>Message:</strong> {item.message}</p>
        </div>
      ))}
      </div>
    </>
  )}
</div>
    </div>
  );
}
