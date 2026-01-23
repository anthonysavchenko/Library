# OSI Model. *From Wikipedia*

[Source](https://en.wikipedia.org/wiki/OSI_model)


## Acronyms

* OSI - Open Systems Interconnection model.
* MAC address - Medium Access Control layer address.
* PPPoE - Point-to-Point Protocol over Ethernet.
* IP - Internet Protocol.
* IPSec - Internet Protocol Security.
* TCP - Transmission Control Protocol.
* UDP - User Datagram Protocol.
* RPC - Remote Procedure Call.
* L2TP - Layer 2 Tunneling Protocol.
* PPTP - Point-to-Point Tunneling Protocol.
* RDP - Remote Desktop Protocol.
* HTTP - HyperText Transfer Protocol.
* SMTP - Simple Mail Transfer Protocol.
* POP3 - Post Office Protocol Version 3.
* IMAP - Internet Message Access Protocol.
* FTP - File Transfer Protocol.
* TELNET - TELetype NETwork.


## Futher reading

* [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call)
* [Network Socket](https://en.wikipedia.org/wiki/Network_socket)
* [HTTP](https://ru.wikipedia.org/wiki/HTTP)
* [SSH](https://ru.wikipedia.org/wiki/SSH)
* [DNS](https://en.wikipedia.org/wiki/Domain_Name_System)


## 

Open Systems Interconnection model (OSI) model is a conseptual model that characterises and standardises the communication functions of a telecommunication or computing system without regard to its underlying internal structure and technology. Its goal is the interoperability of diverse communication systems with standard communication protocols. The model partitions a communication system into abstruction layers.


## Layer 1: Physical Layer

The physical layer is responsible for the transmission and reception of unstructured raw data between a device and a physical transmission medium. It converts the digital bits (1 and 0) into electrical, radio, or optical signals.

Physical layer on the computer is represented with a network adapter.

Protocols: IEEE 802.15 (Bluetooth), IEEE 802.11 Wi-Fi, DSL, IRDA, etc.


## Layer 2: Data Link Layer

The data link layer provides node-to-node data transfer - a link between two directly connected nodes. It detects and possibly corrects errors that may occur in the physical layer. It packs bits from physical layer into frames. Can work with a group of physical layers.

IEEE 802 divides the data link layer into two sublayers:
* Medium access control (MAC) layer - responsible for controlling how devices in a network gain access to a medium and permission to transmit data.
* Logical link control (LLC) layer - responsible for identifying and encapsulating network layer protocols, and controls error checking and frame synchronization.

The local network addresses used in IEEE 802 networks are called media access control (MAC) addresses. MAC address is intended as a unique serial number. MAC addresses are typicaly assigned to network interface hardware at the time of manufacture. The most significant part of the address identifies the manufacturer, who assign the remainder of the address, thus provide a potentially unique address.

In programming data link layer is represented with a network adapter driver.

Protocols: IEEE 802.11 Wi-Fi, Point-to-Point Protocol over Ethernet (PPPoE), etc.


## Layer 3: Network Layer

The network layer is intended to determine a route to transfer data and translate physical network addresses to logical ones.

Protocols: Internet Protocol (IP/IPv4/IPv6), Internet Protocol Security (IPSec), etc.


## Layer 4: Transport Layer

The transport layer is responsible for transfer data from a source to a destination host while maintaining the quality of service. The level of quality varies from one particular protocol to another and depends on protocol class. Some protocols transmit data without reception verification, others guarantee reception, control data sequence, provide error recovery, retransmition, segmentation, reassembly, multiplexing, etc.

The transport layer may be vizualized as post office. A post office inspects only the outer envelope on mail to determine its delivery.

Protocols: Transmission Control Protocol (TCP), User Datagram Protocol (UDP), etc. Although TCP and UDP are not developed under the OSI Reference Model and are not strictly comforming to the OSI definition of the thansport layer.


## Layer 5: Session Layer

The session layer establishes, manages and terminates the connections between the local and remote application. In the OSi model, this layer is responsible for gracefully closing a session, which is handled in the TCP at the transport layer. Session-layer services are commonly used in application environments that make use of remote procedure calls (RPCs).

Protocols: Layer 2 Tunneling Protocol (L2TP), Point-to-Point Tunneling Protocol (PPTP), Remote Procedure Call Protocol (RPC), etc.


## Layer 6: Presentation Layer

The presentation layer provides data transformation from one protocol to another, data encoding and decoding. It transform data from application layer to format which can be transmitted through network. And transform data from network to application layer data format. It also provides data encryption and decription.

In many widely used applications and protocols, no distinction is made between the presentation and application layers. For example, HyperText Transfer Protocol (HTTP), generally regarded as an application-layer protocol, has presentation-layer aspects such as the ability to identify character encoding for proper conversion, which is then done in the application layer.


## Layer 7: Application Layer

The application layer is user interface responsible for displaying received information to the user.

Protocols: RDP, HTTP, SMTP, POP3, FTP, TELNET


## Comparison with TCP/IP model (Internet Protocol Suite)

OSI model | TCP/IP model
----------|-------------
Application layer, Presentation layer, Session layer | Application layer
Session layer, Transport layer | Transport layer
Network layer | Internet layer
Network layer, Data Link layer, Physical layer | Link layer
