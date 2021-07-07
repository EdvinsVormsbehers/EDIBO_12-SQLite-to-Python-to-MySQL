
file_to_write = open('data_out_test.sql', 'w')


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
        i = 0
        for field in fields:
            fields[i] = field.replace("'", "\\'")
            i += 1
        for field in fields[:-1]:
            file_to_write.write(field)
            file_to_write.write("\',\'")
        file_to_write.write(fields[-1])
        file_to_write.write("\'),")
        file_to_write.write('\n')

    fields = data_lines[-1].split('|')
    file_to_write.write("(\'")
    i = 0
    for field in fields:
        fields[i] = field.replace("'", "\\'")
        i += 1
    for field in fields[:-1]:
        file_to_write.write(field)
        file_to_write.write("\',\'")
    file_to_write.write(fields[-1])
    file_to_write.write("\');\n")
    file_to_write.write('\n')


def file2sql(file):
   file_to_read = open(file, "r")
   insert_table_data(file_to_read)
   file_to_read.close()


file_to_write.write("use music_shop;"'\n')
file_to_write.write('\n')
file_to_write.write("SET FOREIGN_KEY_CHECKS=0;"'\n')
file_to_write.write('\n')

insert_command("media_types(MediaTypeId, Name)")
file2sql('data_in_media_types.txt')

insert_command("genres(GenreId, Name)")
file2sql('data_in_genres.txt')

insert_command("artists(ArtistId, Name)")
file2sql('data_in_artists.txt')

insert_command("playlists(PlaylistId, Name)")
file2sql('data_in_playlists.txt')

insert_command("albums(AlbumId, Title, ArtistId)")
file2sql('data_in_albums.txt')

insert_command("tracks(TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice)")
file2sql('data_in_tracks.txt')

insert_command("playlist_track(PlaylistId, TrackId)")
file2sql('data_in_playlist_track.txt')

insert_command("employees(EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email)")
file2sql('data_in_employees.txt')

insert_command("customers(CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId)")
file2sql('data_in_customers.txt')

insert_command("invoices(InvoiceId, CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingCountry, BillingPostalCode, Total)")
file2sql('data_in_invoices.txt')

insert_command("invoice_items(InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity)")
file2sql('data_in_invoice_items.txt')

file_to_write.write("SET FOREIGN_KEY_CHECKS=1;"'\n')
file_to_write.write('\n')

file_to_write.close()
