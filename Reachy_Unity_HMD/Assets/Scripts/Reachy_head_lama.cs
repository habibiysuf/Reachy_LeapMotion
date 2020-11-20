using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class Motorr
{
    public string name;
    public GameObject gameObject;
    public float targetPosition;
    public float presentPosition;
}

public class Reachy_head_lama : MonoBehaviour
{
    
    //public Motorr[] motors;
    //public static Dictionary<string, Motorr> name2motor;
    //public int value;
    //public string nilai;

    //void Start()
    //{
    //    name2motor = new Dictionary<string, Motorr>();

    //    for (int i = 0; i < motors.Length; i++)
    //    {
    //        Motorr m = motors[i];
    //        name2motor[m.name] = m;
    //    }
    //}
    //void Update()
    //{
    //    nilai = HelloRequester.pesan;
    //    value = int.Parse(nilai);
    //    for (int i = 0; i < motors.Length; i++)
    //    {
    //        Motorr m = motors[i];

    //        JointController joint = m.gameObject.GetComponent<JointController>();
    //        joint.RotateTo(value);

    //        m.presentPosition = joint.GetPresentPosition();
    //    }
    //}
}

