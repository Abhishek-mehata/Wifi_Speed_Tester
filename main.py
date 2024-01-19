import speedtest
def test_speed():
    st = speedtest.Speedtest()
    
    download_speed = st.download() / 1_000_000  # Convert to megabits per second
    upload_speed = st.upload() / 1_000_000  # Convert to megabits per second
    ping_speed = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping_speed} ")

if __name__ == "__main__":
    print("Running Speed Test...")
    test_speed()
