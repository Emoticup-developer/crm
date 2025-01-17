import 'package:crm_ui/homepage/homepage.dart';
import 'package:crm_ui/server/server.dart';
import 'package:crm_ui/variable.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class LocalizationPage extends StatefulWidget {
  const LocalizationPage({super.key});

  @override
  State<LocalizationPage> createState() => _LocalizationPageState();
}

class _LocalizationPageState extends State<LocalizationPage> {
  bool isEnabled = false;
  bool isAddMode = false;
  bool isEditMode = false;
  int selected = 0;
  TextEditingController name = TextEditingController();
  TextEditingController description = TextEditingController();
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
                      title: Text("Create Localization"),
                    ),
                  ),
                ],
              ),
            ),
            Visibility(
              visible: isAddMode,
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
                            'Create Localizations',
                            style: TextStyle(
                              color: Colors.black,
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                      SizedBox(height: 16),

                      // Text Field 1
                      TextField(
                        controller: name,
                        decoration: InputDecoration(
                          hintText: 'Enter Name ',
                          filled: true,
                          fillColor: const Color.fromARGB(255, 255, 255, 255),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                            borderSide: BorderSide.none,
                          ),
                          hintStyle: TextStyle(
                              color: const Color.fromARGB(255, 0, 0, 0)),
                        ),
                      ),
                      SizedBox(height: 12),

                      // Text Field 2
                      TextField(
                        controller: description,
                        decoration: InputDecoration(
                          hintText: 'Enter Description',
                          filled: true,
                          fillColor: const Color.fromARGB(255, 255, 255, 255),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                            borderSide: BorderSide.none,
                          ),
                          hintStyle: TextStyle(
                              color: const Color.fromARGB(255, 0, 0, 0)),
                        ),
                      ),
                      SizedBox(height: 12),
                      // Text Field 3
                      TextField(
                        decoration: InputDecoration(
                          hintText: 'Enter third value',
                          filled: true,
                          fillColor: const Color.fromARGB(255, 255, 255, 255),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                            borderSide: BorderSide.none,
                          ),
                          hintStyle: TextStyle(
                              color: const Color.fromARGB(255, 0, 0, 0)),
                        ),
                      ),
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
                            var responce = await http.post(
                                Uri.parse("$url/api/localization_api/"),
                                body: {
                                  "name": name.text,
                                  "description": description.text,
                                  "status": isEnabled.toString(),
                                });
                            print(responce.statusCode);
                            print(responce.body);
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
            ),
            Visibility(
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
                            'update Localizations -> ${name.text}',
                            style: TextStyle(
                              color: Colors.black,
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          GestureDetector(
                            onTap: () {
                              isEditMode = false;
                              setState(() {
                                
                              });
                            },
                            child: Icon(Icons.close_outlined),
                          ),
                        ],
                      ),
                      SizedBox(height: 16),

                      // Text Field 1
                      TextField(
                        controller: name,
                        decoration: InputDecoration(
                          hintText: 'Enter Name ',
                          filled: true,
                          fillColor: const Color.fromARGB(255, 255, 255, 255),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                            borderSide: BorderSide.none,
                          ),
                          hintStyle: TextStyle(
                              color: const Color.fromARGB(255, 0, 0, 0)),
                        ),
                      ),
                      SizedBox(height: 12),

                      // Text Field 2
                      TextField(
                        controller: description,
                        decoration: InputDecoration(
                          hintText: 'Enter Description',
                          filled: true,
                          fillColor: const Color.fromARGB(255, 255, 255, 255),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                            borderSide: BorderSide.none,
                          ),
                          hintStyle: TextStyle(
                              color: const Color.fromARGB(255, 0, 0, 0)),
                        ),
                      ),
                      SizedBox(height: 12),
                      // Text Field 3
                      TextField(
                        decoration: InputDecoration(
                          hintText: 'Enter third value',
                          filled: true,
                          fillColor: const Color.fromARGB(255, 255, 255, 255),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                            borderSide: BorderSide.none,
                          ),
                          hintStyle: TextStyle(
                              color: const Color.fromARGB(255, 0, 0, 0)),
                        ),
                      ),
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
                            var responce = await http.put(
                                Uri.parse(
                                    "$url/api/localization_api/$selected/"),
                                body: {
                                  "name": name.text,
                                  "description": description.text,
                                  "status": isEnabled.toString(),
                                });

                            print(responce.statusCode);
                            print(responce.body);
                            isAddMode = false;

                            isEditMode = false;
                            setState(() {});
                          },
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Colors.amber, // Button color
                          ),
                          child: Text('update'),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
            Visibility(
              visible: !isAddMode,
              child: SingleChildScrollView(
                child: Container(
                  margin: EdgeInsets.all(height * 0.003),
                  child: FutureBuilder(
                    future: fetchData("api/localization_api/"),
                    builder: (context, snapshot) {
                      if (snapshot.connectionState == ConnectionState.waiting) {
                        return Center(child: CircularProgressIndicator());
                      } else if (snapshot.hasError) {
                        return Center(child: Text('Error: ${snapshot.error}'));
                      } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
                        return Center(child: Text('No offices available.'));
                      } else {
                        return Container(
                          width: width * 0.90,
                          margin: EdgeInsets.all(width * 0.003),
                          child: Table(
                            columnWidths: {
                              0: FixedColumnWidth(60),
                              1: FixedColumnWidth(320),
                              2: FixedColumnWidth(300),
                              3: FixedColumnWidth(100),
                              4: FixedColumnWidth(100),
                              5: FixedColumnWidth(60),
                              6: FixedColumnWidth(60),
                            },
                            border: TableBorder.all(
                                width: 0.2, color: Colors.black),
                            children: [
                              TableRow(children: [
                                Padding(
                                  padding: const EdgeInsets.all(4.0),
                                  child: Text(
                                    "SL NO",
                                    style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold),
                                  ),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(4.0),
                                  child: Text(
                                    "Name".toUpperCase(),
                                    style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold),
                                  ),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(4.0),
                                  child: Text(
                                    "Description".toUpperCase(),
                                    style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold),
                                  ),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(4.0),
                                  child: Text(
                                    "STatus".toUpperCase(),
                                    style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold),
                                  ),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(4.0),
                                  child: Text(
                                    "IMAGE".toUpperCase(),
                                    style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold),
                                  ),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(4.0),
                                  child: Text(
                                    "Edit".toUpperCase(),
                                    style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold),
                                  ),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(4.0),
                                  child: Text(
                                    "Delete".toUpperCase(),
                                    style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold),
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
                                        snapshot.data![i]['name'] ?? 'N/A',
                                        style: TextStyle(fontSize: 16),
                                      ),
                                    ),
                                    Padding(
                                      padding: const EdgeInsets.all(4.0),
                                      child: Text(
                                        snapshot.data![i]['description'] ??
                                            'N/A',
                                        style: TextStyle(fontSize: 16),
                                      ),
                                    ),
                                    snapshot.data![i]['status']
                                        ? Container(
                                            color: const Color.fromARGB(
                                                179, 76, 175, 79),
                                            child: Padding(
                                              padding:
                                                  const EdgeInsets.all(4.0),
                                              child: Text(
                                                snapshot.data![i]['status']
                                                    .toString(),
                                                style: TextStyle(
                                                  fontSize: 16,
                                                  color: Colors.white,
                                                ),
                                              ),
                                            ),
                                          )
                                        : Container(
                                            color: const Color.fromARGB(
                                                174, 244, 67, 54),
                                            child: Padding(
                                              padding:
                                                  const EdgeInsets.all(4.0),
                                              child: Text(
                                                snapshot.data![i]['status']
                                                    .toString(),
                                                style: TextStyle(fontSize: 16),
                                              ),
                                            ),
                                          ),
                                    Padding(
                                      padding: const EdgeInsets.all(4.0),
                                      child: Text(
                                        'N/A',
                                        style: TextStyle(fontSize: 16),
                                      ),
                                    ),
                                    GestureDetector(
                                      onTap: () async {
                                        name.text = snapshot.data![i]["name"]
                                            .toString();
                                        description.text = snapshot.data![i]
                                                ["description"]
                                            .toString();
                                        isEnabled = snapshot.data![i]["status"];
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
                                        var responce = await http.delete(Uri.parse(
                                            "$url/api/localization_api/${snapshot.data![i]["id"]}/"));
                                        print(responce.statusCode);
                                        print(responce.body);
                                        setState(() {});
                                      },
                                      child: Padding(
                                        padding: const EdgeInsets.all(4.0),
                                        child: Icon(
                                          Icons.delete_forever_outlined,
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                            ],
                          ),
                        );
                      }
                    },
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
