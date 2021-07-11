from app import app
import callbacks.plot_network_1
import callbacks.plot_network_2
import callbacks.plot_bargraph
import callbacks.tab_callback
import callbacks.slider_update
import callbacks.slider_update_2

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
