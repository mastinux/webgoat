import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.io.ByteArrayOutputStream;
import java.io.ObjectOutputStream;
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.time.LocalDateTime;
import java.nio.charset.StandardCharsets;



class VulnerableTaskHolder implements Serializable {

	private static final long serialVersionUID = 1;

	public String taskName;
	public String taskAction;
	public LocalDateTime requestedExecutionTime;

	public VulnerableTaskHolder(String taskName, String taskAction) {
		super();
		this.taskName = taskName;
		this.taskAction = taskAction;
		this.requestedExecutionTime = LocalDateTime.now();
	}

	private void readObject( ObjectInputStream stream ) throws Exception {
		//deserialize data so taskName and taskAction are available
		stream.defaultReadObject();

		//blindly run some code. #code injection
		Runtime.getRuntime().exec(taskAction);
	}
}



class A8InsecureDeserialization {
	private static void serialize() throws IOException {
		VulnerableTaskHolder go = new VulnerableTaskHolder("sleep for 5 seconds", "sleep 5");

		ByteArrayOutputStream bos = new ByteArrayOutputStream();

		ObjectOutputStream oos = new ObjectOutputStream(bos);
		oos.writeObject(go);
		oos.flush();

		byte[] exploit = bos.toByteArray();
	}

    public static void main(String[] args) throws IOException, ClassNotFoundException {
    	serialize();
    }
}