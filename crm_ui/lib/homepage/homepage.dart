import 'package:crm_ui/Machine/machine.dart';
import 'package:crm_ui/component/component.dart';
import 'package:crm_ui/localization/localization.dart';
import 'package:crm_ui/login/login.dart';
import 'package:crm_ui/product/product.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    final double width = MediaQuery.of(context).size.width;
    final double height = MediaQuery.of(context).size.height;

    return Scaffold(
      appBar: AppBarForAll(context),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "main > dashboard",
              textAlign: TextAlign.left,
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 18,
              ),
            ),
          ),
          Container(
            margin: EdgeInsets.all(width * 0.004),
            width: width,
            height: height * 0.10,
            decoration: BoxDecoration(
              color: Colors.white,
              border: Border.all(
                width: 0.1,
                color: Colors.black,
              ),
            ),
          )
        ],
      ),
      drawer: DrawerForAll(),
    );
  }
}

class DrawerForAll extends StatelessWidget {
  const DrawerForAll({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        children: [
          SizedBox(
            height: MediaQuery.of(context).size.height * 0.04,
          ),
          CircleAvatar(
            radius: 55,
            backgroundColor: Colors.grey,
            child: Icon(
              Icons.person_outline_outlined,
              size: 54,
            ),
          ),
          Center(
            child: Text(
              "administrator",
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          ExpansionTile(
            title: Text(
              "main".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => HomePage(),
                    ),
                  );
                },
                leading: Icon(Icons.dashboard_outlined),
                title: Text("Dashboard"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "master".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => LocalizationPage(),
                    ),
                  );
                },
                leading: Icon(Icons.local_activity_outlined),
                title: Text("Localization"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "catalog".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                onTap: () async {
                  await Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => ProductPage(),
                    ),
                  );
                },
                leading: Icon(Icons.local_shipping_outlined),
                title: Text("Product"),
              ),
              ListTile(
                onTap: () async {
                  await Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => MachinePage(),
                    ),
                  );
                },
                leading: Icon(Icons.device_hub_outlined),
                title: Text("Machine"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "Client".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                leading: Icon(Icons.account_box_outlined),
                title: Text("Account"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "ticket".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                leading: Icon(Icons.edit_document),
                title: Text("Ticket"),
              ),
              ListTile(
                leading: Icon(Icons.device_hub_outlined),
                title: Text("Machine"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "order".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                leading: Icon(Icons.edit_document),
                title: Text("Ticket"),
              ),
              ListTile(
                leading: Icon(Icons.device_hub_outlined),
                title: Text("Machine"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "report".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                leading: Icon(Icons.edit_document),
                title: Text("Ticket"),
              ),
              ListTile(
                leading: Icon(Icons.device_hub_outlined),
                title: Text("Machine"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "request".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                leading: Icon(Icons.edit_document),
                title: Text("Ticket"),
              ),
              ListTile(
                leading: Icon(Icons.device_hub_outlined),
                title: Text("Machine"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "extention".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                leading: Icon(Icons.edit_document),
                title: Text("Ticket"),
              ),
              ListTile(
                leading: Icon(Icons.device_hub_outlined),
                title: Text("Machine"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "user".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                leading: Icon(Icons.edit_document),
                title: Text("Ticket"),
              ),
              ListTile(
                leading: Icon(Icons.device_hub_outlined),
                title: Text("Machine"),
              ),
            ],
          ),
          ExpansionTile(
            title: Text(
              "app component".toUpperCase(),
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 14,
              ),
            ),
            children: [
              ListTile(
                leading: Icon(Icons.edit_document),
                title: Text("Ticket"),
              ),
              ListTile(
                leading: Icon(Icons.device_hub_outlined),
                title: Text("Machine"),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

AppBar AppBarForAll(BuildContext context) {
  return AppBar(
    backgroundColor: const Color.fromARGB(210, 225, 225, 225),
    elevation: 4,
    title: Row(
      children: [
        // App Logo
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 8.0),
          child: Image.asset(
            'assets/logo.png', // Replace with your logo path
            height: 40,
          ),
        ),

        Spacer(),

        // Search Bar
        SizedBox(
          width: 300,
          child: TextField(
            decoration: InputDecoration(
              hintText: 'Search...',
              filled: true,
              fillColor: const Color.fromARGB(255, 206, 206, 206),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(8),
                borderSide: BorderSide.none,
              ),
              prefixIcon:
                  Icon(Icons.search, color: const Color.fromARGB(255, 0, 0, 0)),
            ),
          ),
        ),

        SizedBox(width: 16),

        // Button
        IconButton(
          onPressed: () {
            // Handle button click
          },
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(8),
            ),
          ),
          icon: Icon(Icons.search_outlined),
        ),

        SizedBox(width: 16),

        DropdownButton<String>(
          dropdownColor: const Color.fromARGB(255, 230, 230, 230),
          style: TextStyle(color: Colors.black),
          underline: SizedBox(),
          items: ['Option 1', 'Option 2', 'Option 3']
              .map(
                (option) => DropdownMenuItem<String>(
                  value: option,
                  child: Text(option),
                ),
              )
              .toList(),
          onChanged: (value) {
          
          },
          hint: Text(
            'Select',
            style: TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
          ),
          icon: Icon(Icons.arrow_drop_down,
              color: const Color.fromARGB(255, 0, 0, 0)),
        ),

        SizedBox(width: 16),

        // Notification Icon
        IconButton(
          icon: Icon(Icons.notifications,
              color: const Color.fromARGB(255, 0, 0, 0)),
          onPressed: () {
            // Handle notification click
          },
        ),

        SizedBox(width: 16),

        // Apple Logo
        IconButton(
          icon: Icon(Icons.apple, color: const Color.fromARGB(255, 0, 0, 0)),
          onPressed: () {
            // Handle Apple logo click
          },
        ),

        // Android Logo
        IconButton(
          icon: Icon(Icons.android, color: const Color.fromARGB(255, 0, 0, 0)),
          onPressed: () {
            // Handle Android logo click
          },
        ),

        SizedBox(width: 16),
        GestureDetector(
          onTap: () async {
            await logout();
            await Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => LoginPage(),
              ),
            );
          },
          child: CircleAvatar(
            backgroundColor: const Color.fromARGB(255, 0, 0, 0),
            radius: 18,
            child: Icon(Icons.person, color: Colors.grey[300]),
          ),
        ),
      ],
    ),
  );
}
