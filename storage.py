from google.cloud import storage


def main():
    project_id = "hoge"
    bucket_name = "hoge"

    # make a client instance
    client = storage.Client(project_id)
    # get lists
    buckets = client.get_bucket(bucket_name)
    # print file name
    for file in client.list_blobs(buckets):
        print(file.name)


if __name__ == '__main__':
    main()
