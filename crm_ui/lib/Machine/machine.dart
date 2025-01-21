import 'dart:convert';
import 'dart:io';

import 'package:crm_ui/component/component.dart';
import 'package:crm_ui/homepage/homepage.dart';
import 'package:crm_ui/server/server.dart';
import 'package:crm_ui/variable.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class MachinePage extends StatefulWidget {
  const MachinePage({super.key});

  @override
  State<MachinePage> createState() => _MachinePageState();
}

class _MachinePageState extends State<MachinePage> {
  bool isEnabled = false;
  bool isAddMode = false;
  bool isEditMode = false;
  int selected = 0;
  TextEditingController machine_id = TextEditingController();
  TextEditingController machine_name = TextEditingController();
  TextEditingController attributes = TextEditingController();
  TextEditingController description = TextEditingController();

  bool status = false;
  File? file;
  String filepath = "";
  String filepathonline = "";

  Future<void> uploadMachineData(String filepath, String machine_id,
      String machine_name, String attributes, String status) async {
    var request = http.MultipartRequest('POST', Uri.parse("$url/api/machine/"));

    var file = await http.MultipartFile.fromPath('photo', filepath);

    request.fields["machine_id"] = machine_id;
    request.fields["machine_name"] = machine_name;
    request.fields["attributes"] = attributes;
    request.fields["status"] = status;

    request.files.add(file);

    try {
      var response = await request.send();

      print('Status code: ${response.statusCode}');

      if (response.statusCode == 200 || response.statusCode == 201) {
        var responseBody = await response.stream.bytesToString();
        var jsonResponse = jsonDecode(responseBody);
        print('Response body: $jsonResponse');

        isAddMode = false;
        setState(() {});
      } else {
        print('Error: ${response.statusCode}');
      }
    } catch (e) {
      print('Error: $e');
    }
  }

  Future<void> UpdatedMachineData(String filepath, String machine_id,
      String machine_name, String attributes, String status) async {
    var request =
        http.MultipartRequest('PUT', Uri.parse("$url/api/machine/$selected/"));

    var file = await http.MultipartFile.fromPath('photo', filepath);

    request.fields["machine_id"] = machine_id;
    request.fields["machine_name"] = machine_name;
    // request.fields["attributes"] = attributes;
    request.fields["status"] = status;

    request.files.add(file);

    try {
      var response = await request.send();

      print('Status code: ${response.statusCode}');

      if (response.statusCode == 200 || response.statusCode == 201) {
        var responseBody = await response.stream.bytesToString();
        var jsonResponse = jsonDecode(responseBody);
        print('Response body: $jsonResponse');

        isAddMode = false;
        setState(() {});
      } else {
        print('Error: ${response.statusCode}');
      }
    } catch (e) {
      print('Error: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    final double width = MediaQuery.of(context).size.width;
    final double height = MediaQuery.of(context).size.height;

    return Scaffold(
      appBar: AppBarForAll(context),
      drawer: DrawerForAll(),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              margin: EdgeInsets.all(height * 0.004),
              width: width,
              height: height * 0.10,
              decoration: BoxDecoration(
                border: Border.all(
                  width: 0.1,
                  color: Colors.black,
                ),
                color: Colors.white,
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.end,
                // crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Container(
                    decoration: BoxDecoration(
                      color: const Color.fromARGB(75, 255, 193, 7),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    margin: EdgeInsets.all(width * 0.004),
                    width: width * 0.20,
                    child: ListTile(
                      onTap: () async {
                        isAddMode = isAddMode ? false : true;
                        setState(() {});
                      },
                      leading: Icon(Icons.add_outlined),
                      title: Text("Create Machine"),
                    ),
                  ),
                ],
              ),
            ),
            AddNewMachine(width, height, context),
            EditMachieMachine(width, height, context, filepathonline),
            ShowAllMachine(height, width),
          ],
        ),
      ),
    );
  }

  Visibility EditMachieMachine(double width, double height,
      BuildContext context, String filepathonline) {
    return Visibility(
      visible: isEditMode,
      child: Container(
        width: width * 0.88,
        height: height * 0.80,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Machine ID Field
            TextField(
              enabled: false,
              controller: machine_id,
              decoration: InputDecoration(
                labelText: 'Machine ID',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),

            // Machine Name Field
            TextField(
              controller: machine_name,
              decoration: InputDecoration(
                labelText: 'Machine Name',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),

            // Attributes Field (JSON)

            // SafeArea(
            //   child: Container(
            //     width: width * 0.60,
            //     height: height * 0.30,
            //     child: JsonEditor(
            //       onChanged: (value) {
            //         attributes.text = value;
            //       },
            //       json: jsonEncode(attributes.text),
            //     ),
            //   ),
            // ),

            TextField(
              controller: attributes,
              maxLines: 4,
              decoration: InputDecoration(
                labelText: 'Attributes (JSON)',
                border: OutlineInputBorder(),
                hintText: '{"key1": "value1", "key2": "value2"}',
              ),
            ),
            SizedBox(height: 20),

            // Status Switch
            Row(
              children: [
                Row(
                  children: [
                    Radio<bool>(
                      value: true,
                      groupValue: isEnabled,
                      onChanged: (value) {
                        setState(() {
                          isEnabled = value!;
                        });
                        setState(() {});
                      },
                    ),
                    Text('Enable'),
                  ],
                ),
                SizedBox(width: 16),
                Row(
                  children: [
                    Radio<bool>(
                      value: false,
                      groupValue: isEnabled,
                      onChanged: (value) {
                        setState(() {
                          isEnabled = value!;
                          print(value);
                        });
                        setState(() {});
                      },
                    ),
                    Text('Disable'),
                  ],
                ),
              ],
            ),
            SizedBox(height: 20),

            // Image Picker Button
            Row(
              children: [
                ElevatedButton(
                  onPressed: () async {
                    file = await pickFile();
                    filepath = file!.path.toString();
                    setState(() {
                      print(file!.path.toString());
                    });
                  },
                  child: Text('Upload Image'),
                ),
                SizedBox(width: 10),
                Text(filepath.toString()),
              ],
            ),
            SizedBox(height: 40),
            SafeArea(
              child: Container(
                width: width * 0.10,
                height: height * 0.1,
                child: GestureDetector(
                  onTap: () async {},
                  child: Image.network(
                    "$url/$filepathonline",
                    fit: BoxFit.contain,
                  ),
                ),
              ),
            ),
            // Submit Button
            Center(
              child: Container(
                width: width * 0.30,
                child: CupertinoButton(
                  onPressed: () async {
                    await UpdatedMachineData(filepath, machine_id.text,
                        machine_name.text, attributes.text, status.toString());

                    isAddMode = false;
                    isEditMode = false;
                    setState(() {});
                  },
                  child: Text('Submit'),
                  color: const Color.fromARGB(113, 255, 193, 7),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Visibility AddNewMachine(double width, double height, BuildContext context) {
    return Visibility(
      visible: isAddMode,
      child: Container(
        width: width * 0.88,
        height: height * 0.80,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Machine ID Field
            TextField(
              controller: machine_id,
              decoration: InputDecoration(
                labelText: 'Machine ID',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),

            // Machine Name Field
            TextField(
              controller: machine_name,
              decoration: InputDecoration(
                labelText: 'Machine Name',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),

            // Attributes Field (JSON)
            TextField(
              controller: attributes,
              maxLines: 4,
              decoration: InputDecoration(
                labelText: 'Attributes (JSON)',
                border: OutlineInputBorder(),
                hintText: '{"key1": "value1", "key2": "value2"}',
              ),
            ),
            SizedBox(height: 20),

            // Status Switch
            Row(
              children: [
                Row(
                  children: [
                    Radio<bool>(
                      value: true,
                      groupValue: isEnabled,
                      onChanged: (value) {
                        setState(() {
                          isEnabled = value!;
                        });
                        setState(() {});
                      },
                    ),
                    Text('Enable'),
                  ],
                ),
                SizedBox(width: 16),
                Row(
                  children: [
                    Radio<bool>(
                      value: false,
                      groupValue: isEnabled,
                      onChanged: (value) {
                        setState(() {
                          isEnabled = value!;
                          print(value);
                        });
                        setState(() {});
                      },
                    ),
                    Text('Disable'),
                  ],
                ),
              ],
            ),
            SizedBox(height: 20),

            // Image Picker Button
            Row(
              children: [
                ElevatedButton(
                  onPressed: () async {
                    file = await pickFile();
                    filepath = file!.path.toString();
                    setState(() {
                      print(file!.path.toString());
                    });
                  },
                  child: Text('Upload Image'),
                ),
                SizedBox(width: 10),
                Text(filepath.toString()),
              ],
            ),
            SizedBox(height: 40),

            // Submit Button
            Center(
              child: ElevatedButton(
                onPressed: () async {
                  await uploadMachineData(filepath, machine_id.text,
                      machine_name.text, attributes.text, status.toString());

                  isAddMode = false;
                  setState(() {});
                },
                child: Text('Submit'),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Visibility ShowAllMachine(double height, double width) {
    return Visibility(
      visible: !isAddMode,
      child: SingleChildScrollView(
        child: Container(
          margin: EdgeInsets.all(height * 0.003),
          child: FutureBuilder(
            future: fetchData("api/machine/"),
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                return Center(child: CircularProgressIndicator());
              } else if (snapshot.hasError) {
                return Center(child: Text('Error: ${snapshot.error}'));
              } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
                return Center(child: Text('No offices available.'));
              } else {
                return Container(
                  width: width * 0.96,
                  margin: EdgeInsets.all(width * 0.003),
                  child: SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Table(
                      columnWidths: {
                        0: FixedColumnWidth(60),
                        1: FixedColumnWidth(120),
                        2: FixedColumnWidth(300),
                        3: FixedColumnWidth(150),
                        4: FixedColumnWidth(100),
                        5: FixedColumnWidth(250),
                        6: FixedColumnWidth(100),
                      },
                      border: TableBorder.all(width: 0.2, color: Colors.black),
                      children: [
                        TableRow(children: [
                          Padding(
                            padding: const EdgeInsets.all(4.0),
                            child: Text(
                              "SL NO",
                              style: TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(4.0),
                            child: Text(
                              "Machine ID".toUpperCase(),
                              style: TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(4.0),
                            child: Text(
                              "Machine Name".toUpperCase(),
                              style: TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(4.0),
                            child: Text(
                              "Photo".toUpperCase(),
                              style: TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(4.0),
                            child: Text(
                              "Status".toUpperCase(),
                              style: TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(4.0),
                            child: Text(
                              "created_at".toUpperCase(),
                              style: TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(4.0),
                            child: Text(
                              "Edit".toUpperCase(),
                              style: TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                          ),
                        ]),
                        for (int i = 0; i < snapshot.data!.length; i++)
                          TableRow(
                            children: [
                              Padding(
                                padding: const EdgeInsets.all(4.0),
                                child: Text(
                                  "${i + 1}".toString(),
                                  style: TextStyle(fontSize: 16),
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.all(4.0),
                                child: Text(
                                  snapshot.data![i]['machine_id'].toString() ??
                                      'N/A',
                                  style: TextStyle(fontSize: 16),
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.all(4.0),
                                child: Text(
                                  snapshot.data![i]['machine_name']
                                          .toString() ??
                                      'N/A',
                                  style: TextStyle(fontSize: 16),
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.all(4.0),
                                child: GestureDetector(
                                  onTap: () {
                                    void showImageDialog(
                                        BuildContext context, String imageUrl) {
                                      showDialog(
                                        context: context,
                                        builder: (BuildContext context) {
                                          return AlertDialog(
                                            content: Column(
                                              mainAxisSize: MainAxisSize.min,
                                              children: [
                                                Image.network(
                                                    "$url/$imageUrl"), // Image from URL
                                                SizedBox(height: 20),
                                                ElevatedButton(
                                                  onPressed: () {
                                                    Navigator.of(context)
                                                        .pop(); // Close the dialog
                                                  },
                                                  child: Text("Close"),
                                                ),
                                              ],
                                            ),
                                          );
                                        },
                                      );
                                    }

                                    showImageDialog(context,
                                        snapshot.data![i]["photo"].toString());
                                  },
                                  child: Text(
                                    "View".toString() ?? 'N/A',
                                    style: TextStyle(
                                        fontSize: 16,
                                        color: const Color.fromARGB(
                                            255, 0, 64, 117)),
                                  ),
                                ),
                              ),
                              if (snapshot.data![i]['status'])
                                Container(
                                  color:
                                      const Color.fromARGB(255, 139, 236, 142),
                                  child: Padding(
                                    padding: const EdgeInsets.all(4.0),
                                    child: Text(
                                      snapshot.data![i]['status'].toString() ??
                                          'N/A',
                                      style: TextStyle(fontSize: 16),
                                    ),
                                  ),
                                )
                              else
                                Container(
                                  color: const Color.fromARGB(76, 247, 33, 18),
                                  child: Padding(
                                    padding: const EdgeInsets.all(4.0),
                                    child: Text(
                                      snapshot.data![i]['status'].toString() ??
                                          'N/A',
                                      style: TextStyle(fontSize: 16),
                                    ),
                                  ),
                                ),
                              Padding(
                                padding: const EdgeInsets.all(4.0),
                                child: Text(
                                  snapshot.data![i]['created_at'].toString() ??
                                      'N/A',
                                  style: TextStyle(fontSize: 16),
                                ),
                              ),
                              Row(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceEvenly,
                                crossAxisAlignment: CrossAxisAlignment.center,
                                children: [
                                  GestureDetector(
                                    onTap: () async {
                                      machine_id.text = snapshot.data![i]
                                              ["machine_id"]
                                          .toString();

                                      machine_name.text =
                                          snapshot.data![i]["machine_name"];

                                      attributes.text = snapshot.data![i]
                                              ["attributes"]
                                          .toString();

                                      isEnabled = snapshot.data![i]["status"];
                                      filepathonline =
                                          snapshot.data![i]["photo"];
                                      selected = snapshot.data![i]["id"];
                                      isEditMode = true;
                                      isAddMode = false;

                                      setState(() {});
                                    },
                                    child: Padding(
                                      padding: const EdgeInsets.all(4.0),
                                      child: Icon(
                                        Icons.edit_outlined,
                                      ),
                                    ),
                                  ),
                                  GestureDetector(
                                    onTap: () async {
                                      machine_id.text = snapshot.data![i]
                                              ["machine_id"]
                                          .toString();

                                      machine_name.text =
                                          snapshot.data![i]["machine_name"];

                                      attributes.text = jsonEncode(snapshot.data![i]
                                              ["attributes"]
                                          .toString());

                                      isEnabled = snapshot.data![i]["status"];
                                      filepathonline =
                                          snapshot.data![i]["photo"];
                                      selected = snapshot.data![i]["id"];
                                      isEditMode = false;
                                      isAddMode = true;

                                      setState(() {});
                                    },
                                    child: Padding(
                                      padding: const EdgeInsets.all(4.0),
                                      child: Icon(
                                        Icons.copy_outlined,
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                      ],
                    ),
                  ),
                );
              }
            },
          ),
        ),
      ),
    );
  }

  Visibility EditMachine(double width) {
    return Visibility(
      visible: isEditMode,
      child: Container(
        padding: EdgeInsets.all(width * 0.004),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Dialog Title with Close Button
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    'Create Product',
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  GestureDetector(
                    onTap: () {
                      isEditMode = false;
                      setState(() {});
                    },
                    child: Icon(Icons.close_outlined),
                  ),
                ],
              ),
              SizedBox(height: 16),

              // Text Field 1
              TextField(
                // controller: product_code,
                decoration: InputDecoration(
                  hintText: 'Enter Product Code ',
                  filled: true,
                  fillColor: const Color.fromARGB(255, 255, 255, 255),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(8),
                    borderSide: BorderSide.none,
                  ),
                  hintStyle:
                      TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
                ),
              ),
              SizedBox(height: 12),

              // Text Field 2
              TextField(
                // controller: product_title,
                decoration: InputDecoration(
                  hintText: 'Enter Product Title',
                  filled: true,
                  fillColor: const Color.fromARGB(255, 255, 255, 255),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(8),
                    borderSide: BorderSide.none,
                  ),
                  hintStyle:
                      TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
                ),
              ),
              SizedBox(height: 12),

              SizedBox(height: 12),
              Row(
                children: [
                  Row(
                    children: [
                      Radio<bool>(
                        value: true,
                        groupValue: isEnabled,
                        onChanged: (value) {
                          setState(() {
                            isEnabled = value!;
                          });
                          setState(() {});
                        },
                      ),
                      Text('Enable'),
                    ],
                  ),
                  SizedBox(width: 16),
                  Row(
                    children: [
                      Radio<bool>(
                        value: false,
                        groupValue: isEnabled,
                        onChanged: (value) {
                          setState(() {
                            isEnabled = value!;
                            print(value);
                          });
                          setState(() {});
                        },
                      ),
                      Text('Disable'),
                    ],
                  ),
                ],
              ),
              // Submit Button
              Align(
                alignment: Alignment.centerRight,
                child: ElevatedButton(
                  onPressed: () async {
                    var request = http.MultipartRequest(
                        'POST', Uri.parse("$url/api/machine/"));
                    var file =
                        await http.MultipartFile.fromPath('photo', filepath);
                    request.fields["machine_id"] = machine_id.toString();
                    request.fields["machine_name"] = machine_name.toString();
                    request.fields["attributes"] = attributes.text.toString();
                    request.fields["status"] = status.toString();
                    request.files.add(file);
                    var response = await request.send();
                    print(response.statusCode);
                    print(response.stream);
                    isAddMode = false;
                    setState(() {});
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.amber, // Button color
                  ),
                  child: Text('Submit'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
