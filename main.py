file_to_read_albums = open('data_in_albums.txt', 'r')
file_to_read_artists = open('data_in_artists.txt', 'r')
file_to_read_customers = open('data_in_customers.txt', 'r')
file_to_read_employees = open('data_in_employees.txt', 'r')
file_to_read_genres = open('data_in_genres.txt', 'r')
file_to_read_invoice_items = open('data_in_invoice_items.txt', 'r')
file_to_read_invoices = open('data_in_invoices.txt', 'r')
file_to_read_media_types = open('data_in_media_types.txt', 'r')
file_to_read_playlist_track = open('data_in_playlist_track.txt', 'r')
file_to_read_playlists = open('data_in_playlists.txt', 'r')
file_to_read_tracks = open('data_in_tracks.txt', 'r')

file_to_write = open('data_out.sql', 'w')


def insert_command(table_name):
    file_to_write.write("insert into " + table_name + '\n')
    file_to_write.write("values"'\n')


def insert_table_data(file_to_read):
    data = file_to_read.read()
    # print("Result after - file_to_read_albums.read():")
    # print(type(data))
    # print(data)

    data_lines = data.split('\n')[:-1]
    # print("Result after - data.split(\'\n\')[:-1]:")
    # print(type(data_lines))
    # print(data_lines)

    for line in data_lines[:-1]:
        # print(line.split('|'))
        fields = line.split('|')
        file_to_write.write("(\'")
        for field in fields[:-1]:
            field = field.replace("'", "")
            file_to_write.write(field)
            file_to_write.write("\',\'")
        fields[-1] = fields[-1].replace("'", "")
        file_to_write.write(fields[-1])
        file_to_write.write("\'),")
        file_to_write.write('\n')

    fields = data_lines[-1].split('|')
    file_to_write.write("(\'")
    for field in fields[:-1]:
        field = field.replace("'", "")
        file_to_write.write(field)
        file_to_write.write("\',\'")
    fields[-1] = fields[-1].replace("'", "")
    file_to_write.write(fields[-1])
    file_to_write.write("\');\n")
    file_to_write.write('\n')


file_to_write.write("use music_shop;"'\n')
file_to_write.write('\n')

insert_command("albums(AlbumId, Title, ArtistId)")
insert_table_data(file_to_read_albums)
insert_command("artists(ArtistId, Name)")
insert_table_data(file_to_read_artists)
insert_command("customers(CostumerId, FirstName, LastName, Company, Address, City, State, Country, PostelCode, Phone, Fax, Email, SuportRepId)")
insert_table_data(file_to_read_customers)
insert_command("employees(EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostelCode, Phone, Fax, Email)")
insert_table_data(file_to_read_employees)
insert_command("genres(GenreId, Name)")
insert_table_data(file_to_read_genres)
insert_command("invoice_items(InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity)")
insert_table_data(file_to_read_invoice_items)
insert_command("invoices(InvoiceId, CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingCountry, BillingPostalCode, Total)")
insert_table_data(file_to_read_invoices)
insert_command("media_types(MediaTypeId, Name)")
insert_table_data(file_to_read_media_types)
insert_command("playlist_tracks(PlaylistId, TrackId, PK_PlaylistTrack)")
insert_table_data(file_to_read_playlist_track)
insert_command("playlists(PlaylistId, Name)")
insert_table_data(file_to_read_playlists)
insert_command("tracks(TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice)")
insert_table_data(file_to_read_tracks)

file_to_read_albums.close()
file_to_read_artists.close()
file_to_read_customers.close()
file_to_read_employees.close()
file_to_read_genres.close()
file_to_read_invoice_items.close()
file_to_read_invoices.close()
file_to_read_media_types.close()
file_to_read_playlist_track.close()
file_to_read_playlists.close()
file_to_read_tracks.close()

file_to_write.close()
